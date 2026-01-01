# app/core/sentiment.py

POSITIVE_WORDS = {
    "good", "great", "awesome", "love", "happy", "excellent", "nice"
}

NEGATIVE_WORDS = {
    "bad", "terrible", "hate", "sad", "worst", "angry"
}


def analyze_sentiment(text: str) -> str:
    text = text.lower()

    positive_score = sum(word in text for word in POSITIVE_WORDS)
    negative_score = sum(word in text for word in NEGATIVE_WORDS)

    if positive_score >= negative_score:
        return "positive"
    return "negative"
