import ast
import os

class ControllerAnalyzer:
    """Parses Python controllers with Enterprise detail (docstrings & type hints)."""
    
    def analyze_file(self, file_path):
        with open(file_path, "r") as f:
            tree = ast.parse(f.read())
            
        data = {"methods": {}}
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                # We capture docstrings so the AI knows 'WHY' the code exists
                docstring = ast.get_docstring(node)
                args = [arg.arg for arg in node.args.args]
                
                data["methods"][node.name] = {
                    "parameters": args,
                    "description": docstring or "No documentation provided.",
                    "line_number": node.lineno
                }
        return data