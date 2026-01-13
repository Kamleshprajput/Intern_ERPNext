def compare_snapshots(old, new):
    report = {"new_doctypes": [], "changed_fields": {}, "changed_methods": {}}

    # Compare Schema (DocTypes)
    for dt, fields in new["schema"].items():
        if dt not in old["schema"]:
            report["new_doctypes"].append(dt)
        elif set(fields) != set(old["schema"][dt]):
            report["changed_fields"][dt] = {
                "added": list(set(fields) - set(old["schema"][dt])),
                "removed": list(set(old["schema"][dt]) - set(fields))
            }

    # Compare Logic (Python methods)
    for path, logic in new["logic"].items():
        if path in old["logic"]:
            old_classes = old["logic"][path]["classes"]
            for cls, methods in logic["classes"].items():
                if cls in old_classes:
                    added = set(methods) - set(old_classes[cls])
                    removed = set(old_classes[cls]) - set(methods)
                    if added or removed:
                        report["changed_methods"][f"{path}::{cls}"] = {
                            "added": list(added), "removed": list(removed)
                        }
    return report