from flask import Flask, request, jsonify
from sentiment_analysis import analyze_sentiment
import pandas as pd

app = Flask(__name__)

# Route to analyze sentiment
@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    if not data or 'text' not in data:
        return jsonify({'error': 'Invalid input'}), 400

    sentiment = analyze_sentiment(data['text'])
    return jsonify({'sentiment': sentiment})

if __name__ == '__main__':
    app.run(debug=True)
