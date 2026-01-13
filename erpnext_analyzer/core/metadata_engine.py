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

            fields = data.get("fields", [])
            # Handle both list and dict formats
            if isinstance(fields, list):
                fields_list = [
                    {
                        "fieldname": f.get("fieldname") if isinstance(f, dict) else str(f),
                        "fieldtype": f.get("fieldtype") if isinstance(f, dict) else "Unknown",
                        "label": f.get("label") if isinstance(f, dict) else "",
                        "reqd": f.get("reqd", 0) if isinstance(f, dict) else 0
                    }
                    for f in fields
                ]
            else:
                fields_list = []
            
            permissions = data.get("permissions", [])
            if isinstance(permissions, list):
                permissions_list = [
                    {"role": p.get("role") if isinstance(p, dict) else str(p), 
                     "read": p.get("read") if isinstance(p, dict) else 0}
                    for p in permissions
                ]
            else:
                permissions_list = []
            
            return {
                "name": data.get("name"),
                "module": data.get("module"),
                "is_submittable": data.get("is_submittable", 0),
                "fields": fields_list,
                "permissions": permissions_list
            }
        except Exception as e:
            return {"error": str(e)}