import torch
from ai.model_loader import load_model

# Load model once
tokenizer, model, id2label = load_model()

def ai_predict(text: str):
    inputs = tokenizer(
        text,
        return_tensors="pt",
        truncation=True,
        padding=True,
        max_length=512
    )

    with torch.no_grad():
        outputs = model(**inputs)

    probs = torch.nn.functional.softmax(outputs.logits, dim=-1)[0]

    # Dynamically find spam/phishing index
    spam_index = next(
        (int(i) for i, v in id2label.items()
         if "spam" in v.lower() or "phish" in v.lower()),
        1
    )

    return float(probs[spam_index])
