from flask import Flask, request, render_template, jsonify
import pickle
from PIL import Image
import numpy as np
import io
import tensorflow as tf

app = Flask(__name__)

# Load the model
with open('./notebooks/model.pkl', 'rb') as file:
    model = pickle.load(file)

# Preprocess image
def preprocess_image(image):
    image = image.resize((128, 128))  # Adjust size as per model input
    image = np.array(image) / 255.0   # Normalize
    image = np.expand_dims(image, axis=0)  # Add batch dimension
    return image

@app.route('/')
def home():
    return render_template('./templates/index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400

    try:
        image = Image.open(io.BytesIO(file.read())).convert('RGB')
        processed_image = preprocess_image(image)
        prediction = model.predict(processed_image)
        result = 'Malaria Positive' if prediction[0][0] > 0.5 else 'Malaria Negative'
        return jsonify({'prediction': result})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)