from flask import Flask, request, jsonify
from tensorflow.keras.models import load_model
import numpy as np

app = Flask(__name__)  # Corrected Flask instantiation

# Loading the model
model = load_model("D:\\ML PROJECTS\\Market_maestro\\models\\Marketmaestro_1.0.h5")

def preprocess_text(text):
    # Placeholder for the actual preprocessing steps
    # Replace with real preprocessing logic for tokenization, encoding, etc.
    return np.array([text])  # Adjust this line according to your model's requirements

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    text = data.get("text", "")

    # Preprocess the input text for the model
    processed_text = preprocess_text(text)

    # Make prediction
    prediction = model.predict(processed_text)[0][0]  # Adjust index if needed

    # Convert prediction to a human-readable format
    sentiment = "Positive" if prediction >= 0.5 else "Negative"

    return jsonify({'prediction': sentiment})

if __name__ == '__main__':
    app.run(debug=True)
