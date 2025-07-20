#CodexVigil to run in the background as an active "AI"
# CodexVigil.py
#note: Monitors the DropZone folder and analyzes any new Python scripts dropped into it.

import os
import time
import hashlib
from datetime import datetime

#note: Configuration
WATCH_DIR = r"D:\Atlas\_DropZone"
LOG_DIR = r"D:\Atlas\CodexVigil\logs"
PROCESSED_DIR = os.path.join(WATCH_DIR, "_processed")
CHECK_INTERVAL = 10  # Seconds

#note: Ensure log and processed folders exist
os.makedirs(LOG_DIR, exist_ok=True)
os.makedirs(PROCESSED_DIR, exist_ok=True)

def hash_file(filepath):
    #note: Prevent reprocessing the same file
    with open(filepath, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()

def analyze_script(filepath):
    analysis = {
        "filename": os.path.basename(filepath),
        "timestamp": datetime.now().isoformat(),
        "lines": 0,
        "todos": [],
        "functions": [],
        "imports": [],
        "errors": [],
    }

    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                analysis["lines"] += 1
                if line.startswith("# TODO") or "TODO" in line:
                    analysis["todos"].append(line)
                if line.startswith("def "):
                    analysis["functions"].append(line)
                if line.startswith("import ") or line.startswith("from "):
                    analysis["imports"].append(line)

    except Exception as e:
        analysis["errors"].append(str(e))

    return analysis

def log_analysis(data):
    log_path = os.path.join(LOG_DIR, f"{data['filename']}_{int(time.time())}.log")
    with open(log_path, 'w', encoding='utf-8') as log:
        for k, v in data.items():
            if isinstance(v, list):
                log.write(f"{k.upper()}:\n")
                for item in v:
                    log.write(f"  - {item}\n")
            else:
                log.write(f"{k.upper()}: {v}\n")
        log.write("\n--- End of Log ---\n")

def run():
    print(f"[CodexVigil] Watching {WATCH_DIR} every {CHECK_INTERVAL}s...")
    seen_hashes = set()

    while True:
        for filename in os.listdir(WATCH_DIR):
            if filename.endswith(".py"):
                filepath = os.path.join(WATCH_DIR, filename)
                file_hash = hash_file(filepath)

                if file_hash not in seen_hashes:
                    print(f"[+] Processing new file: {filename}")
                    result = analyze_script(filepath)
                    log_analysis(result)
                    os.rename(filepath, os.path.join(PROCESSED_DIR, filename))
                    seen_hashes.add(file_hash)

        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    run()