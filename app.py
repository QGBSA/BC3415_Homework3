# app.py
from flask import Flask, render_template, request
from sentiment_analysis import analyze_sentiment
from image_video_generation import generate_image_from_prompt

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
        image_path = generate_image_from_prompt(prompt)
        return render_template('generate_image.html', image_path=image_path)
    return render_template('generate_image.html')

# Add this route to handle video generation
@app.route('/generate_video', methods=['GET', 'POST'])
def generate_video():
    if request.method == 'POST':
        prompt = request.form['prompt']
        video_path = generate_video_from_prompt(prompt)  # Assuming you have a function for video generation
        return render_template('generate_video.html', video_path=video_path)
    return render_template('generate_video.html')


if __name__ == "__main__":
    app.run(debug=True)
