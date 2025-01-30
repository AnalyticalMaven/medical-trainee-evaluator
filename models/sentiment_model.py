from transformers import pipeline

sentiment_pipeline = pipeline(
    "sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english"
)

def analyze_tone(text):
    """Analyze tone from text"""
    result = sentiment_pipeline(text)[0]
    return {
        "tone": result["label"],
        "confidence": result["score"]
    }