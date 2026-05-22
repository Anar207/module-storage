import os

HISTORY_FILE = "history.txt"

def save_history(operation, result):
    with open(HISTORY_FILE, "a", encoding="utf-8") as f:
        f.write(f"{operation} = {result}\n")

def load_history():
    if not os.path.exists(HISTORY_FILE):
        return []
    with open(HISTORY_FILE, "r", encoding="utf-8") as f:
        return [line.strip() for line in f.readlines()]
