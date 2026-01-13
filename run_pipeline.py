import ast
import os
import json
from erpnext_analyzer.core.metadata_engine import SchemaAnalyzer
from erpnext_analyzer.core.controller_engine import ControllerAnalyzer
def generate_ai_context_package(app_path):
    # 1. Initialize Engines
    schema_eng = SchemaAnalyzer()
    logic_eng = ControllerAnalyzer()
    
    full_inventory = {}

    # 2. Walk through the ERPNext structure
    # ERPNext stores things in: erpnext/[module]/doctype/[name]/...
    for root, dirs, files in os.walk(app_path):
        if "doctype" in root:
            doctype_name = os.path.basename(root)
            full_inventory[doctype_name] = {}
            
            for file in files:
                if file.endswith(".json"):
                    full_inventory[doctype_name]["schema"] = schema_eng.analyze_json(os.path.join(root, file))
                if file.endswith(".py") and file != "__init__.py":
                    full_inventory[doctype_name]["logic"] = logic_eng.analyze_file(os.path.join(root, file))
                    
    return full_inventory