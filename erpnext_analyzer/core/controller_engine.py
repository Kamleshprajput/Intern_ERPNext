import ast
import os
class ControllerEngine:
    def analyze(self, py_path):
        """Parses Python controllers to map methods and API endpoints."""
        try:
            with open(py_path, "r", encoding="utf-8") as f:
                tree = ast.parse(f.read())
            
            analysis = {
                "methods": [],
                "imports": []
            }

            for node in ast.walk(tree):
                # Capture imports to understand dependencies
                if isinstance(node, (ast.Import, ast.ImportFrom)):
                    analysis["imports"].append(ast.dump(node))

                # Capture Class methods
                if isinstance(node, ast.FunctionDef):
                    # Check for @frappe.whitelist() decorator
                    # Handles: @frappe.whitelist(), @frappe.whitelist(allow_guest=True), etc.
                    is_whitelisted = False
                    for d in node.decorator_list:
                        # Handle @frappe.whitelist() - ast.Call with ast.Attribute
                        if isinstance(d, ast.Call):
                            if isinstance(d.func, ast.Attribute) and d.func.attr == 'whitelist':
                                is_whitelisted = True
                                break
                        # Handle @whitelist (direct name)
                        elif isinstance(d, ast.Name) and d.id == 'whitelist':
                            is_whitelisted = True
                            break
                        # Handle @frappe.whitelist (attribute without call)
                        elif isinstance(d, ast.Attribute) and d.attr == 'whitelist':
                            is_whitelisted = True
                            break
                    
                    analysis["methods"].append({
                        "name": node.name,
                        "is_api": is_whitelisted,
                        "args": [a.arg for a in node.args.args if a.arg != 'self'],
                        "doc": ast.get_docstring(node) or "No docstring provided."
                    })
            return analysis
        except Exception as e:
            return {"error": str(e)}