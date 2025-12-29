import re

def heuristic_score(text: str):
    text = text.lower()
    score = 0.0

    keywords = [
        "verify", "urgent", "account", "password",
        "login", "confirm", "bank", "restricted"
    ]

    for k in keywords:
        if k in text:
            score += 0.08

    if len(re.findall(r"https?://\S+", text)) > 1:
        score += 0.2

    return min(score, 1.0)
