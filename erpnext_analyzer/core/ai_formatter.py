class AIFormatter:
    def format_for_prompt(self, inventory):
        markdown = "# ERPNext App Intelligence Snapshot\n\n"
        
        # App Info
        if 'repo_info' in inventory:
            markdown += f"## App Information\n"
            markdown += f"- **Path:** {inventory['repo_info'].get('app_path', 'N/A')}\n"
            markdown += f"- **Commit:** {inventory['repo_info'].get('commit', 'N/A')}\n\n"
        
        # Hooks
        if 'global_hooks' in inventory and inventory['global_hooks']:
            markdown += "## Global Hooks\n"
            for hook_name, hook_data in inventory['global_hooks'].items():
                if hook_data and hook_data != "Registered":
                    markdown += f"- **{hook_name}:** {str(hook_data)[:100]}...\n"
                else:
                    markdown += f"- **{hook_name}:** Registered\n"
            markdown += "\n"
        
        # DocTypes
        if 'doctypes' in inventory:
            markdown += "## DocTypes\n\n"
            for dt, data in inventory['doctypes'].items():
                markdown += f"### {dt}\n"
                if 'schema' in data and data['schema']:
                    schema = data['schema']
                    markdown += f"- **Module:** {schema.get('module', 'N/A')}\n"
                    markdown += f"- **Submittable:** {schema.get('is_submittable', 0)}\n"
                    if 'fields' in schema:
                        fields = ", ".join([f.get('fieldname', '') for f in schema['fields'][:10]])
                        markdown += f"- **Fields:** {fields}...\n"
                if 'logic' in data and data['logic']:
                    if isinstance(data['logic'], dict) and 'methods' in data['logic']:
                        api_methods = [m['name'] for m in data['logic']['methods'] if m.get('is_api')]
                        all_methods = [m['name'] for m in data['logic']['methods']]
                        if api_methods:
                            markdown += f"- **API Methods:** {', '.join(api_methods)}\n"
                        markdown += f"- **All Methods:** {', '.join(all_methods[:10])}...\n"
                markdown += "\n"
        
        # API Endpoints
        if 'api_endpoints' in inventory and inventory['api_endpoints']:
            markdown += "## Custom API Endpoints\n"
            for api in inventory['api_endpoints']:
                markdown += f"- **{api['module']}:** {len(api.get('methods', []))} methods\n"
            markdown += "\n"
        
        # Custom Modules
        if 'custom_modules' in inventory and inventory['custom_modules']:
            markdown += "## Custom Modules\n"
            for module, files in inventory['custom_modules'].items():
                markdown += f"- **{module}:** {len(files)} files\n"
            markdown += "\n"
        
        # Fixtures
        if 'fixtures' in inventory and inventory['fixtures']:
            markdown += f"## Fixtures ({len(inventory['fixtures'])} found)\n\n"
        
        return markdown