class AIFormatter:
    def format_for_prompt(self, inventory):
        markdown = "# ERPNext App Intelligence Snapshot\n\n"
        for dt, data in inventory['doctypes'].items():
            markdown += f"## DocType: {dt}\n"
            if 'schema' in data:
                fields = ", ".join([f['name'] for f in data['schema']['fields'][:5]])
                markdown += f"- **Key Fields:** {fields}...\n"
            if 'logic' in data:
                methods = ", ".join([m['name'] for m in data['logic']])
                markdown += f"- **Methods:** {methods}\n"
            markdown += "\n"
        return markdown