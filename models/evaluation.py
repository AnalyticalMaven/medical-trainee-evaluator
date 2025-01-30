def evaluate_performance(transcription):
    text = transcription.lower()
    empathy_keywords = ["how are you", "feel", "comfortable", "understand"]
    context_keywords = ["treatment", "diagnosis", "symptoms", "medication"]
    
    empathy_score = sum(1 for keyword in empathy_keywords if keyword in text) / len(empathy_keywords)
    context_score = sum(1 for keyword in context_keywords if keyword in text) / len(context_keywords)
    
    return {"empathy": round(empathy_score, 2), "context": round(context_score, 2)}