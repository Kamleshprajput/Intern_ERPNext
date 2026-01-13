import os
import json
from erpnext_analyzer.core.metadata_engine import MetadataEngine
from erpnext_analyzer.core.controller_engine import ControllerEngine
from erpnext_analyzer.core.hook_engine import HookEngine
from erpnext_analyzer.core.snapshot_connector import SnapshotConnector
from erpnext_analyzer.core.ai_formatter import AIFormatter

# CONFIGURATION
REPO_PATH = r"../"
OUTPUT_DIR = "snapshots"

def run_all():
    if not os.path.exists(OUTPUT_DIR): os.makedirs(OUTPUT_DIR)
    
    # Init Engines
    meta_eng = MetadataEngine()
    ctrl_eng = ControllerEngine()
    hook_eng = HookEngine()
    conn = SnapshotConnector(os.path.dirname(REPO_PATH))
    formatter = AIFormatter()
    
    inventory = {
        "repo_info": {"commit": conn.get_latest_commit()},
        "doctypes": {},
        "global_hooks": hook_eng.analyze(os.path.join(REPO_PATH, "hooks.py"))
    }

    print("🛠️ Analyzing System...")

    for root, _, files in os.walk(REPO_PATH):
        if "doctype" in root:
            dt_name = os.path.basename(root)
            inventory["doctypes"][dt_name] = {}
            for file in files:
                fpath = os.path.join(root, file)
                if file.endswith(".json"):
                    inventory["doctypes"][dt_name]["schema"] = meta_eng.analyze(fpath)
                elif file.endswith(".py") and "__init__" not in file:
                    inventory["doctypes"][dt_name]["logic"] = ctrl_eng.analyze(fpath)

    # Save RAW JSON
    with open(f"{OUTPUT_DIR}/raw_snapshot.json", "w") as f:
        json.dump(inventory, f, indent=4)

    # Save AI-Optimized Markdown
    with open(f"{OUTPUT_DIR}/ai_ready_context.md", "w") as f:
        f.write(formatter.format_for_prompt(inventory))
    
    print(f"✅ Success! AI context generated in /{OUTPUT_DIR}")

if __name__ == "__main__":
    run_all()