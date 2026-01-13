import ast
import os
class HookEngine:
    def analyze(self, hooks_path):
        """Parses hooks.py to map event-driven logic and app configuration."""
        if not os.path.exists(hooks_path): 
            return {}
            
        try:
            with open(hooks_path, "r", encoding="utf-8") as f:
                tree = ast.parse(f.read())
            
            hooks_map = {}
            # ERPNext hooks are top-level assignments (e.g., doc_events = {...})
            for node in tree.body:
                if isinstance(node, ast.Assign):
                    for target in node.targets:
                        if isinstance(target, ast.Name):
                            key = target.id
                            # Focus on the most critical AI-relevant hooks
                            if key in ['doc_events', 'scheduler_events', 'override_whitelisted_methods', 'fixtures']:
                                hooks_map[key] = "Registered" 
            return hooks_map
        except Exception as e:
            return {"error": str(e)}