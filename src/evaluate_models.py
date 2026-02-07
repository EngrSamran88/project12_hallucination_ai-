import csv
from utils import load_tasks
from metrics import is_correct

MODELS = ["code-llama", "starcoder", "llama-v1"]

def generate_code(model, prompt):
    """
    Placeholder: Replace with actual API calls
    """
    return "GENERATED_CODE"

def run_model_tests():
    tasks = load_tasks()
    rows = []
    for model in MODELS:
        for task in tasks:
            out = generate_code(model, task["description"])
            ok = is_correct(out, task["expected_output"])
            rows.append({
                "model": model,
                "task": task["id"],
                "output": out,
                "correct": ok
            })
    return rows

def write_csv(results, file="results/analysis.csv"):
    with open(file, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=results[0].keys())
        writer.writeheader()
        writer.writerows(results)

if __name__ == "__main__":
    results = run_model_tests()
    write_csv(results)
