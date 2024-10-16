# sentiment_analysis.py
from transformers import pipeline  # Example using Hugging Face's pipeline for sentiment analysis

def analyze_sentiment(text):
    """
    Analyzes the sentiment of the input text and returns the sentiment score or label.
    
    Args:
    - text (str): The input text to analyze.

    Returns:
    - str: The sentiment label, e.g., "Positive", "Negative", or "Neutral".
    """
    # Load the sentiment-analysis pipeline (you can load it outside the function for efficiency)
    sentiment_pipeline = pipeline("sentiment-analysis")
    
    # Analyze the text
    result = sentiment_pipeline(text)
    
    # Extract and return sentiment label
    sentiment_label = result[0]['label']
    return sentiment_label
