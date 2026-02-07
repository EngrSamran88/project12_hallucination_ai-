def is_correct(output, expected):
    return output.strip() == expected.strip()

def analyze_failures(results):
    """
    Tabulate different types of hallucination patterns
    """
    patterns = {}
    for r in results:
        label = r["failure_type"]
        patterns[label] = patterns.get(label, 0) + 1
    return patterns
