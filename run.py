import json
from erpnext_analyzer.core.parser import ERPNextParser
from erpnext_analyzer.core.diff import compare_snapshots

# Paths to your locally cloned ERPNext repo (different versions)
REPO_V14 = "./erpnext_v14"
REPO_V15 = "./erpnext_v15"

def run_analysis():
    print("Parsing V14...")
    p14 = ERPNextParser(REPO_V14)
    snap14 = p14.generate_snapshot()

    print("Parsing V15...")
    p15 = ERPNextParser(REPO_V15)
    snap15 = p15.generate_snapshot()

    print("Generating structural diff...")
    diff = compare_snapshots(snap14, snap15)

    with open("erpnext_analyzer/snapshots/diff_report.json", "w") as f:
        json.dump(diff, f, indent=4)
    
    print("Report generated in snapshots/diff_report.json")

if __name__ == "__main__":
    run_analysis()