import subprocess
from pathlib import Path

#Find most recently modified .py file, will exclude push_single.py
latest_file = max(
    [f for f in Path(".").glob("*.py") if f.name != "push_single.py"],
    key=lambda f: f.stat().st_mtime
)

#Promt commit message
message = input(f"Commit message for '{latest_file.name}': ").strip()
if not message:
    message = f"Update {latest_file.name}"

#Git commands
commands = [
    ["git", "add", latest_file.name],
    ["git", "commit", "-m", message],
    ["git", "push"]
]

for cmd in commands:
    result = subprocess.run(cmd, capture_output=True, text=True)
    print(result.stdout.strip())
    if result.stderr:
        print("⚠️", result.stderr.strip())