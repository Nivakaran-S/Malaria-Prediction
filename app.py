from flask import Flask, request, render_template, jsonify
import pickle
from PIL import Image
import numpy as np
import io
import tensorflow as tf
import os

app = Flask(__name__)

# Load the model
with open('./final_model/model.pkl', 'rb') as file:
    model = pickle.load(file)

# Preprocess image
def preprocess_image(image):
    target_size = (224, 224)  # match model's expected input size
    image = image.resize(target_size)
    image = np.array(image, dtype=np.float32) / 255.0  # normalize to 0-1
    image = np.expand_dims(image, axis=0)  # add batch dimension
    return image

@app.route('/')
def home():
    return render_template('index.html')

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

        # Make prediction
        prediction = model.predict(processed_image)
        probability = float(prediction[0][0])  # convert to native float

        # Get label
        result_label = 'Malaria Positive' if probability > 0.5 else 'Malaria Negative'
        
        # Convert probability to percentage
        probability_percent = round(probability * 100, 2)

        return jsonify({
            'prediction': result_label,
            'confidence': f"{probability_percent} %"
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
