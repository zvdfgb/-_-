import sys

def parse_changes(file_list):
    has_test = any("test" in f for f in file_list)
    has_docs = any(f.endswith(".md") for f in file_list)
    has_py = any(f.endswith(".py") and "test" not in f for f in file_list)
    
    scope = "core" if has_py else ("docs" if has_docs else "test")
    c_type = "feat" if has_py else ("docs" if has_docs else "test")
    return f"{c_type}({scope}): auto-generated conventional commit from staged files"

changed_files = ["src/model.py", "tests/test_model.py"]
print("Detected changes:", changed_files)
print("Generated Commit Msg:\n" + parse_changes(changed_files))
