import os
import json
try:
    import yaml
except ImportError:
    yaml = None
from erpnext_analyzer.core.metadata_engine import MetadataEngine
from erpnext_analyzer.core.controller_engine import ControllerEngine
from erpnext_analyzer.core.hook_engine import HookEngine
from erpnext_analyzer.core.snapshot_connector import SnapshotConnector
from erpnext_analyzer.core.ai_formatter import AIFormatter

# CONFIGURATION
# Load config from config.yaml if it exists
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_FILE = os.path.join(BASE_DIR, "config.yaml")

APP_BASE_PATH = None
if os.path.exists(CONFIG_FILE) and yaml:
    try:
        with open(CONFIG_FILE, 'r') as f:
            config = yaml.safe_load(f) or {}
            app_path_config = config.get('app_path')
            # Handle empty string, None, or null
            if app_path_config and str(app_path_config).strip() and str(app_path_config).lower() != 'null':
                APP_BASE_PATH = app_path_config
                # If relative path, make it relative to config file location
                if not os.path.isabs(APP_BASE_PATH):
                    APP_BASE_PATH = os.path.normpath(os.path.join(BASE_DIR, APP_BASE_PATH))
    except Exception as e:
        print(f"[WARNING] Could not read config.yaml: {e}")
elif os.path.exists(CONFIG_FILE) and not yaml:
    print(f"[INFO] config.yaml found but PyYAML not installed. Install with: pip install pyyaml")

# If APP_BASE_PATH is set, validate it
if APP_BASE_PATH and os.path.exists(APP_BASE_PATH) and os.path.isdir(APP_BASE_PATH):
    # Check if the configured path itself is the app (has hooks.py)
    hooks_file = os.path.join(APP_BASE_PATH, "hooks.py")
    if os.path.exists(hooks_file):
        # The configured path IS the app directory
        REPO_PATH = os.path.normpath(APP_BASE_PATH)
        print(f"[INFO] Using configured app path: {REPO_PATH}")
    else:
        # Check if it's a directory containing app subdirectories (like erpnext_v14/erpnext)
        # Look for common app directory patterns
        potential_apps = []
        try:
            for item in os.listdir(APP_BASE_PATH):
                item_path = os.path.join(APP_BASE_PATH, item)
                if os.path.isdir(item_path):
                    hooks_file = os.path.join(item_path, "hooks.py")
                    if os.path.exists(hooks_file):
                        potential_apps.append((item, item_path))
        except:
            pass
        
        if potential_apps:
            print(f"[INFO] Found {len(potential_apps)} potential app(s) in {APP_BASE_PATH}:")
            for name, path in potential_apps:
                print(f"  - {name}: {path}")
            print(f"[INFO] Using first found app: {potential_apps[0][1]}")
            REPO_PATH = os.path.normpath(potential_apps[0][1])
        else:
            # Use the configured path as-is
            REPO_PATH = os.path.normpath(APP_BASE_PATH)
            print(f"[WARNING] Using configured path: {REPO_PATH}")
            print(f"[WARNING] hooks.py not found. This may not be a valid Frappe app directory.")
elif not APP_BASE_PATH:
    # Auto-detection: try to find the app directory automatically
    PARENT_DIR = os.path.dirname(BASE_DIR)
    GRANDPARENT_DIR = os.path.dirname(PARENT_DIR)  # Go up to "verilog" directory
    
    # Auto-detection: look for any Frappe app directories
    alt_paths = [
        # Check in current directory for app subdirectories
        os.path.join(BASE_DIR, "erpnext_v14", "erpnext"),
        os.path.join(BASE_DIR, "erpnext_v15", "erpnext"),
        # Check relative to parent
        os.path.join(PARENT_DIR, "Intern_ERPNext", "intern_erpnext"),
        os.path.join(PARENT_DIR, "intern_erpnext"),
        os.path.join(PARENT_DIR, "Intern_ERPNext"),
        # Check in grandparent (verilog directory)
        os.path.join(GRANDPARENT_DIR, "Intern_ERPNext", "intern_erpnext"),
        os.path.join(GRANDPARENT_DIR, "intern_erpnext"),
        os.path.join(GRANDPARENT_DIR, "Intern_ERPNext"),
    ]
    
    print("[INFO] Auto-detecting app directory...")
    for alt_path in alt_paths:
        normalized_path = os.path.normpath(alt_path)
        if os.path.exists(normalized_path) and os.path.isdir(normalized_path):
            # Verify it's a Frappe app by checking for hooks.py
            hooks_file = os.path.join(normalized_path, "hooks.py")
            if os.path.exists(hooks_file):
                APP_BASE_PATH = normalized_path
                print(f"[INFO] Found app at: {APP_BASE_PATH}")
                break
    
    if not APP_BASE_PATH:
        print("[WARNING] Could not auto-detect app directory.")
        print("[INFO] Please set 'app_path' in config.yaml to point to your Intern_ERPNext/intern_erpnext directory")
        REPO_PATH = None
    else:
        REPO_PATH = os.path.normpath(APP_BASE_PATH)
else:
    REPO_PATH = os.path.normpath(APP_BASE_PATH) if APP_BASE_PATH else None

OUTPUT_DIR = "snapshots"

def run_all():
    if not os.path.exists(OUTPUT_DIR): os.makedirs(OUTPUT_DIR)
    
    # Validate path
    if not os.path.exists(REPO_PATH):
        print(f"[ERROR] App path not found: {REPO_PATH}")
        print(f"Please update APP_BASE_PATH in run_pipeline.py to point to your Intern_ERPNext/intern_erpnext directory")
        return
    
    print(f"[OK] Found app at: {REPO_PATH}")
    
    # Init Engines
    meta_eng = MetadataEngine()
    ctrl_eng = ControllerEngine()
    hook_eng = HookEngine()
    conn = SnapshotConnector(os.path.dirname(REPO_PATH))
    formatter = AIFormatter()
    
    inventory = {
        "repo_info": {"commit": conn.get_latest_commit(), "app_path": REPO_PATH},
        "doctypes": {},
        "global_hooks": hook_eng.analyze(os.path.join(REPO_PATH, "hooks.py")),
        "api_endpoints": [],
        "fixtures": [],
        "custom_modules": {}
    }

    print("[*] Analyzing System...")
    print(f"[*] Scanning: {REPO_PATH}")

    # Walk through the app directory
    for root, dirs, files in os.walk(REPO_PATH):
        rel_path = os.path.relpath(root, REPO_PATH)
        
        # Analyze DocTypes
        if "doctype" in root:
            dt_name = os.path.basename(root)
            if dt_name not in inventory["doctypes"]:
                inventory["doctypes"][dt_name] = {}
            for file in files:
                fpath = os.path.join(root, file)
                if file.endswith(".json"):
                    inventory["doctypes"][dt_name]["schema"] = meta_eng.analyze(fpath)
                elif file.endswith(".py") and "__init__" not in file:
                    if "logic" not in inventory["doctypes"][dt_name]:
                        inventory["doctypes"][dt_name]["logic"] = []
                    logic_data = ctrl_eng.analyze(fpath)
                    if logic_data and "error" not in logic_data:
                        inventory["doctypes"][dt_name]["logic"] = logic_data
        
        # Process all files in current directory
        for file in files:
            fpath = os.path.join(root, file)
            
            # Capture api.py files (custom API endpoints)
            if file == "api.py" and root != REPO_PATH:
                api_data = ctrl_eng.analyze(fpath)
                if api_data and "error" not in api_data:
                    inventory["api_endpoints"].append({
                        "module": rel_path.replace(os.sep, "."),
                        "path": fpath,
                        "methods": api_data.get("methods", [])
                    })
            
            # Capture fixtures directory
            if "fixtures" in root and (file.endswith("_fixture.json") or file.endswith(".json")):
                inventory["fixtures"].append({
                    "path": fpath,
                    "relative_path": rel_path,
                    "file": file
                })
        
        # Capture custom modules (Python files in module directories)
        if rel_path and rel_path != "." and "doctype" not in rel_path:
            module_name = rel_path.replace(os.sep, ".")
            for file in files:
                if file.endswith(".py") and file != "__init__.py" and file != "api.py":
                    py_path = os.path.join(root, file)
                    if module_name not in inventory["custom_modules"]:
                        inventory["custom_modules"][module_name] = []
                    mod_data = ctrl_eng.analyze(py_path)
                    if mod_data and "error" not in mod_data:
                        inventory["custom_modules"][module_name].append({
                            "file": file,
                            "methods": mod_data.get("methods", [])
                        })

    # Save RAW JSON
    with open(f"{OUTPUT_DIR}/raw_snapshot.json", "w") as f:
        json.dump(inventory, f, indent=4)

    # Save AI-Optimized Markdown
    with open(f"{OUTPUT_DIR}/ai_ready_context.md", "w") as f:
        f.write(formatter.format_for_prompt(inventory))
    
    print(f"[SUCCESS] AI context generated in /{OUTPUT_DIR}")

if __name__ == "__main__":
    run_all()