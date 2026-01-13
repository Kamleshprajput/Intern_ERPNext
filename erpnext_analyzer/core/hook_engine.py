import ast
import os

class HookEngine:
    def _extract_dict_structure(self, node):
        """Recursively extracts dictionary structure from AST."""
        if isinstance(node, ast.Dict):
            result = {}
            for k, v in zip(node.keys, node.values):
                if isinstance(k, (ast.Str, ast.Constant)):
                    key = k.s if isinstance(k, ast.Str) else k.value
                    if isinstance(v, ast.Dict):
                        result[key] = self._extract_dict_structure(v)
                    elif isinstance(v, ast.List):
                        result[key] = [self._extract_list_item(item) for item in v.elts]
                    elif isinstance(v, (ast.Str, ast.Constant)):
                        result[key] = v.s if isinstance(v, ast.Str) else v.value
                    else:
                        result[key] = "Complex expression"
            return result
        return None
    
    def _extract_list_item(self, item):
        """Extracts list items from AST."""
        if isinstance(item, (ast.Str, ast.Constant)):
            return item.s if isinstance(item, ast.Str) else item.value
        elif isinstance(item, ast.Dict):
            return self._extract_dict_structure(item)
        return "Complex expression"
    
    def analyze(self, hooks_path):
        """Parses hooks.py to map event-driven logic and app configuration."""
        if not os.path.exists(hooks_path): 
            return {}
            
        try:
            with open(hooks_path, "r", encoding="utf-8") as f:
                content = f.read()
                tree = ast.parse(content)
            
            hooks_map = {}
            # ERPNext hooks are top-level assignments (e.g., doc_events = {...})
            for node in tree.body:
                if isinstance(node, ast.Assign):
                    for target in node.targets:
                        if isinstance(target, ast.Name):
                            key = target.id
                            # Focus on the most critical AI-relevant hooks
                            if key in ['doc_events', 'scheduler_events', 'override_whitelisted_methods', 
                                      'fixtures', 'app_name', 'app_version', 'app_title', 'app_description',
                                      'app_publisher', 'app_icon', 'app_color', 'app_logo_url', 'app_url',
                                      'before_install', 'after_install', 'before_uninstall', 'after_uninstall',
                                      'on_session_creation', 'on_logout', 'on_login', 'has_permission',
                                      'permission_query_conditions', 'override_doctype_class']:
                                # Try to extract the actual structure
                                if isinstance(node.value, ast.Dict):
                                    hooks_map[key] = self._extract_dict_structure(node.value)
                                elif isinstance(node.value, ast.List):
                                    hooks_map[key] = [self._extract_list_item(item) for item in node.value.elts]
                                elif isinstance(node.value, (ast.Str, ast.Constant)):
                                    hooks_map[key] = node.value.s if isinstance(node.value, ast.Str) else node.value.value
                                else:
                                    hooks_map[key] = "Registered (complex expression)"
            return hooks_map
        except Exception as e:
            return {"error": str(e)}