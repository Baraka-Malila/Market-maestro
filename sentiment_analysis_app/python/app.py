# app.py
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    text = data.get("text", "")

    # Hardcoded response for now
    sentiment = "Positive" if "good" in text.lower() else "Negative"
    return jsonify({'prediction': sentiment})

if __name__ == '__main__':
    app.run(debug=True)
