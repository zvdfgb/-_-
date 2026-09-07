import json, sys

mock_agent_response = '''{
  "thought": "Analysis completed",
  "action": "patch",
  "files_modified": ["core.py"],
  "exit_code": 0
}'''

try:
    data = json.loads(mock_agent_response)
    required_keys = {"thought", "action", "files_modified", "exit_code"}
    if not required_keys.issubset(data.keys()):
        raise ValueError("Missing required contract keys")
    print(f"[Contract VALID] Action: {data['action']}, Target: {data['files_modified']}")
except Exception as e:
    print(f"[Contract ERROR] {e}", file=sys.stderr)
    sys.exit(1)
