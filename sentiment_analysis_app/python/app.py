from flask import Flask, request, jsonify, render_template

app = Flask(__name__, template_folder='templates', static_folder='static')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    text = data.get("text", "")

    if not text:
        return jsonify({'error': 'No text provided'}), 400

    sentiment = "Positive" if "good" in text.lower() else "Negative"
    return jsonify({'prediction': sentiment})

if __name__ == '__main__':
    app.run(debug=True)
