POSITIVE_WORDS = {"good", "great", "excellent", "happy", "love"}
NEGATIVE_WORDS = {"bad", "terrible", "sad", "hate", "poor"}

def sentiment_score(text: str) -> int:
    words = text.lower().split()
    score = sum(1 for w in words if w in POSITIVE_WORDS) - sum(1 for w in words if w in NEGATIVE_WORDS)
    return score
