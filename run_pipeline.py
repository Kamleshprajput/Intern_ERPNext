import os
from erpnext_analyzer.core.parser import ERPNextParser

# Use absolute paths to avoid any "No Output" confusion
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_PATH = os.path.join(BASE_DIR, "Intern_ERPNext")

def test_discovery(path):
    print(f"--- Discovery Test for: {path} ---")
    py_files = []
    json_files = []
    for root, _, files in os.walk(path):
        for f in files:
            if f.endswith(".py"): py_files.append(f)
            if f.endswith(".json"): json_files.append(f)
    
    print(f"Found {len(py_files)} Python files.")
    print(f"Found {len(json_files)} JSON files.")
    
    if not py_files and not json_files:
        print("ERROR: No files found! Check if the folder 'Intern_ERPNext' is in the same directory as this script.")

if __name__ == "__main__":
    test_discovery(REPO_PATH)
    # If the above prints numbers > 0, proceed to parsing:
    # parser = ERPNextParser(REPO_PATH)
    # ... rest of your code ...