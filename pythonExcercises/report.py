
def generate_report(data: dict) -> str:
    filtered = {name: score for name, score in data.items() if score >= 80}
    if not filtered:
        return "No students scored 80 or above."
    lines = ["Student Report (80+):"]
    for name, score in sorted(filtered.items()):
        lines.append(f"{name}: {score}")
    return "\n".join(lines)