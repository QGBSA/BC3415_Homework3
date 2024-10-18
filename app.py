from flask import Flask, render_template, request
from sentiment_analysis import analyze_sentiment

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

if __name__ == "__main__":
    app.run(debug=True)
