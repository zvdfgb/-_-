import re, sys

issue_content = """
### Environment
- OS: Windows 11
- Python: 3.13

### Reproduction Steps
1. Run `sdt-greet --name " "`

### Expected vs Actual
Expected exit 2, actually got exit 0 with empty name.
"""

required_sections = ["Environment", "Reproduction Steps", "Expected vs Actual"]
for sec in required_sections:
    if not re.search(rf"###\s+{re.escape(sec)}", issue_content):
        print(f"[REJECT] Missing required section: {sec}")
        sys.exit(1)

print("[PASSED] Issue description satisfies all quality gates.")
