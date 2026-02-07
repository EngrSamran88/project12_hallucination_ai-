import json

def load_tasks(path="data/tasks.json"):
    with open(path) as f:
        return json.load(f)
