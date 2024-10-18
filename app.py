from flask import Flask, render_template, request
from sentiment_analysis import analyze_sentiment
from image_generation import generate_image_from_prompt  # Ensure this import points to your updated function

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

# Sentiment analysis route
@app.route('/sentiment', methods=['GET', 'POST'])
def sentiment():
    if request.method == 'POST':
        text_input = request.form['text']
        sentiment_result = analyze_sentiment(text_input)
        return render_template('sentiment.html', result=sentiment_result)
    return render_template('sentiment.html')

# Image generation route
@app.route('/generate_image', methods=['GET', 'POST'])
def generate_image():
    if request.method == 'POST':
        prompt = request.form['prompt']
        image_url = generate_image_from_prompt(prompt)
        return render_template('generate_image.html', image_url=image_url)
    return render_template('generate_image.html')

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=True)
