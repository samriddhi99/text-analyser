import re

def clean_text(text: str) -> str:
    text = text.lower()
    return re.sub(r'[^a-z\s]', '', text)
