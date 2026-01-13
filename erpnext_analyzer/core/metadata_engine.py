import json
import os

class MetadataEngine:
    def analyze(self, json_path):
        """Extracts schema, field types, and naming rules from DocType JSON."""
        if not os.path.exists(json_path): 
            return None
        try:
            with open(json_path, "r", encoding="utf-8") as f:
                data = json.load(f)
            
            # We filter for 'DocType' to avoid parsing workspace or dashboard JSONs
            if data.get("doctype") != "DocType":
                return None

            return {
                "name": data.get("name"),
                "module": data.get("module"),
                "is_submittable": data.get("is_submittable", 0),
                "fields": [
                    {
                        "fieldname": f.get("fieldname"),
                        "fieldtype": f.get("fieldtype"),
                        "label": f.get("label"),
                        "reqd": f.get("reqd", 0)
                    }
                    for f in data.get("fields", [])
                ],
                "permissions": [
                    {"role": p.get("role"), "read": p.get("read")}
                    for p in data.get("permissions", [])
                ]
            }
        except Exception as e:
            return {"error": str(e)}