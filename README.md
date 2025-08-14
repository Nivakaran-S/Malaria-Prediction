# 🦟 Malaria Detection Web App

A deep learning–powered **Flask web application** that detects malaria from blood smear images with high accuracy.  
This project integrates a **trained convolutional neural network (CNN)** with an intuitive web interface, allowing medical professionals, researchers, and enthusiasts to upload an image and receive both the prediction and the model's confidence level.

---

## 🚀 Features

- **Deep Learning Model** – Trained on high-quality malaria dataset using TensorFlow/Keras.
- **Real-Time Predictions** – Upload a blood smear image and get instant results.
- **Confidence Score** – Shows probability percentage for the predicted result.
- **Clean UI** – Minimal, professional web interface built with Flask + HTML/CSS.
- **REST API Support** – Returns predictions as JSON, making it easy to integrate into other systems.

---

## 📂 Project Structure

```bash

MalariaDetection/
│── app.py # Main Flask application
│── requirements.txt # Python dependencies
│── templates/
│ └── index.html # Frontend template
│── final_model/ # Place downloaded model here
│── static/ # (Optional) CSS, JS, images
│── README.md # Project documentation

```


---

## 📦 Installation & Setup

### 1️⃣ Clone the repository
```bash
git clone https://github.com/yourusername/MalariaDetection.git
cd MalariaDetection
```

### 2️⃣ Create and activate a virtual environment

```bash 

python -m venv venv
venv\Scripts\activate   # Windows
# or
source venv/bin/activate  # Mac/Linux

```

### 3️⃣ Install dependencies

```bash 

pip install -r requirements.txt

```

### 4️⃣ Download the trained model

Download the pre-trained model from Google Drive:

🔗 Download Model Here[https://drive.google.com/drive/folders/1HVz_um6LN6xJ8BwW5splbZqf_4-r7XUx?usp=drive_link]

Unzip (if compressed) and place the model file inside the final_model directory:
```bash

MalariaDetection/
│── final_model/
│    └── model.pkl

```

### 5️⃣ Run the Flask app
```bash 

python app.py

```
The app will run locally at:

```bash

http://127.0.0.1:5000/

```

---

## 🌐 Usage

1. Open the app in your browser.
2. Upload a blood smear image (JPEG/PNG format).
3. Get:
    - Prediction: "Malaria Positive" or "Malaria Negative".
    - Confidence: Probability percentage of the result.
4. Or send a POST request to /predict with file in multipart/form-data to get a JSON response.

---

## 🧠 Model Details
- Architecture: Convolutional Neural Network (CNN)
- Input Size: 224×224×3 RGB images
- Output: Binary classification (Positive / Negative)
- Training Data: Public malaria cell image dataset
- Framework: TensorFlow/Keras
- Performance: High accuracy & robust to common variations in microscopy images

---

## 🔍 Example API Request

```bash

curl -X POST -F "file=@sample_image.png" http://127.0.0.1:5000/predict

```

Example JSON Response:

```bash

{
  "prediction": "Malaria Positive",
  "confidence": "97.85 %"
}

```

---

## 🎯 Why This Project Stands Out

- Combines AI + Web Development seamlessly.
- Demonstrates end-to-end deployment skills (data → model → API → frontend).
- Uses real medical imaging data for a socially impactful application.
- UI designed for a clean, responsive look.
- Code is modular, clean, and production-ready.

---

## 🤝 Contributions
Contributions, issues, and feature requests are welcome!
Feel free to fork this repo and submit pull requests.