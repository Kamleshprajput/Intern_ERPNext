import ast
import json
import os

class ERPNextParser:
    def __init__(self, repo_path):
        self.repo_path = repo_path

    def get_py_ast(self, file_path):
        """Extracts methods and class definitions from Python files."""
        with open(file_path, 'r') as f:
            try:
                tree = ast.parse(f.read())
                logic = {"classes": {}}
                for node in ast.walk(tree):
                    if isinstance(node, ast.ClassDef):
                        methods = [m.name for m in node.body if isinstance(m, ast.FunctionDef)]
                        logic["classes"][node.name] = methods
                return logic
            except Exception:
                return None

    def get_doctype_fields(self, json_path):
        """Extracts field names from DocType JSON metadata."""
        with open(json_path, 'r') as f:
            try:
                data = json.load(f)
                if data.get("doctype") == "DocType":
                    return [field.get("fieldname") for field in data.get("fields", [])]
            except Exception:
                return None
        return None

    def generate_snapshot(self):
        snapshot = {"logic": {}, "schema": {}}
        for root, _, files in os.walk(self.repo_path):
            for file in files:
                full_path = os.path.join(root, file)
                rel_path = os.path.relpath(full_path, self.repo_path)

                if file.endswith(".py"):
                    res = self.get_py_ast(full_path)
                    if res: snapshot["logic"][rel_path] = res

                elif file.endswith(".json") and "doctype" in root.lower():
                    res = self.get_doctype_fields(full_path)
                    if res:
                        # Extract the DocType name from the file name
                        dt_name = file.replace(".json", "")
                        snapshot["schema"][dt_name] = res
        return snapshot