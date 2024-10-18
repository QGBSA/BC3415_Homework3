'''
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk

# Initialize the sentiment analyzer
sia = SentimentIntensityAnalyzer()

def analyze_sentiment(text):
    """
    Analyzes the sentiment of the input text using NLTK's VADER tool and returns the sentiment score or label.

    Args:
    - text (str): The input text to analyze.

    Returns:
    - str: The sentiment label, e.g., "Positive", "Negative", or "Neutral".
    """
    # Get the sentiment scores for the text
    scores = sia.polarity_scores(text)
    
    # Classify based on compound score
    if scores['compound'] >= 0.05:
        return "Positive"
    elif scores['compound'] <= -0.05:
        return "Negative"
    else:
        return "Neutral"
'''
'''
from transformers import pipeline  # Example using Hugging Face's pipeline for sentiment analysis

# Load the sentiment-analysis pipeline once
sentiment_pipeline = pipeline("sentiment-analysis")

def analyze_sentiment(text):
    """
    Analyzes the sentiment of the input text and returns the sentiment score or label.
    
    Args:
    - text (str): The input text to analyze.

    Returns:
    - str: The sentiment label, e.g., "Positive", "Negative", or "Neutral".
    """
    # Analyze the text
    result = sentiment_pipeline(text)
    
    # Extract and return sentiment label
    sentiment_label = result[0]['label']
    return sentiment_label
'''

import transformers

def analyze_sentiment(text):
    model = transformers.pipeline("sentiment-analysis")
    result = model(text)
    sentiment_label = result[0]['label']
    return sentiment_label
