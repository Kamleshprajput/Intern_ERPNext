import json

class SchemaAnalyzer:
    """Parses DocType JSON files to understand the data structure."""
    
    def analyze_json(self, json_path):
        with open(json_path, "r") as f:
            meta = json.load(f)
            
        return {
            "name": meta.get("name"),
            "module": meta.get("module"),
            "fields": [
                {"name": f.get("fieldname"), "type": f.get("fieldtype"), "label": f.get("label")}
                for f in meta.get("fields", [])
            ],
            "permissions": meta.get("permissions", [])
        }
