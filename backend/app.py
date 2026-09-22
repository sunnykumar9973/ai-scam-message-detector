"""
Flask Backend API for Scam Message Detection
Serves predictions from the trained ML model via REST API

API Flow:
1. Frontend sends POST request with message text
2. Flask loads pre-trained model and vectorizer
3. Text is converted to TF-IDF features
4. Logistic Regression predicts class and confidence
5. Result is returned as JSON
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import os
import numpy as np
import re

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Enable Cross-Origin requests from React frontend

# Paths to saved model and vectorizer
MODEL_DIR = os.path.join(os.path.dirname(__file__), "..", "model")
MODEL_FILE = os.path.join(MODEL_DIR, "scam_detector_model.pkl")
VECTORIZER_FILE = os.path.join(MODEL_DIR, "tfidf_vectorizer.pkl")

# Global variables to store loaded model and vectorizer
model = None
vectorizer = None

def load_model_and_vectorizer():
    """Load the pre-trained model and vectorizer from disk"""
    global model, vectorizer
    
    try:
        if not os.path.exists(MODEL_FILE) or not os.path.exists(VECTORIZER_FILE):
            raise FileNotFoundError(
                f"Model files not found. Please run: python dataset/train_model.py"
            )
        
        model = joblib.load(MODEL_FILE)
        vectorizer = joblib.load(VECTORIZER_FILE)
        
        print("✓ Model and vectorizer loaded successfully")
        return True
    
    except Exception as e:
        print(f"✗ Error loading model: {e}")
        return False

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        "status": "healthy",
        "message": "Scam Detector API is running"
    }), 200

@app.route('/predict', methods=['POST'])
def predict():
    """
    Main prediction endpoint
    
    Request:
        POST /predict
        Content-Type: application/json
        {
            "message": "string to classify"
        }
    
    Response:
        {
            "prediction": "Safe" or "Scam",
            "probability": [safe_prob, scam_prob],
            "confidence": 95,
            "is_scam": boolean
        }
    """
    
    try:
        # Get JSON data from request
        data = request.get_json()
        
        if not data or 'message' not in data:
            return jsonify({
                "error": "Message field is required"
            }), 400
        
        message = data.get('message', '').strip()
        
        # Validate input
        if not message:
            return jsonify({
                "error": "Message cannot be empty"
            }), 400
        
        if len(message) > 5000:
            return jsonify({
                "error": "Message too long (max 5000 characters)"
            }), 400
        
        # Convert message to TF-IDF features
        message_tfidf = vectorizer.transform([message])

        # Get prediction from model
        prediction = model.predict(message_tfidf)[0]
        probabilities = model.predict_proba(message_tfidf)[0].astype(float)

        # Simple rule-based booster to help capture obvious scam signals
        # Detect URLs and spammy keywords and increase scam probability slightly
        rule_score = 0.0
        # URL detection
        if re.search(r'https?://\S+|www\.\S+', message, flags=re.IGNORECASE):
            rule_score += 0.30

        # Keyword signals (each occurrence adds a small boost, capped)
        spam_keywords = [
            'congrat', 'won', 'prize', 'claim', 'free', 'urgent', 'verify', 'click', 'winner', 'selected', 'cash'
        ]
        found = 0
        low_msg = message.lower()
        for kw in spam_keywords:
            if kw in low_msg:
                found += 1

        rule_score += min(0.08 * found, 0.30)

        # Apply rule_score to scam probability and renormalize
        scam_prob = float(probabilities[1]) + rule_score
        safe_prob = float(probabilities[0])
        # Prevent probabilities > 1 and renormalize
        if scam_prob + safe_prob > 0:
            total = scam_prob + safe_prob
            scam_prob = scam_prob / total
            safe_prob = safe_prob / total

        # Final prediction and formatting
        is_scam = bool(scam_prob >= 0.5)
        confidence = int(max(scam_prob, safe_prob) * 100)

        response = {
            "prediction": "🚨 Scam" if is_scam else "✅ Safe",
            "is_scam": is_scam,
            "confidence": confidence,
            "probability": {
                "safe": int(safe_prob * 100),
                "scam": int(scam_prob * 100)
            },
            "algorithm": "Logistic Regression with TF-IDF (+ simple rule boosts)"
        }
        
        return jsonify(response), 200
    
    except Exception as e:
        return jsonify({
            "error": f"Prediction failed: {str(e)}"
        }), 500

@app.route('/info', methods=['GET'])
def info():
    """Return model information"""
    return jsonify({
        "model_name": "Scam Message Detector",
        "version": "1.0",
        "algorithm": "Logistic Regression with TF-IDF Vectorization",
        "description": "Classifies SMS messages as Safe (Ham) or Scam (Spam)",
        "input_format": "Plain text message",
        "output": "Classification + confidence score",
        "endpoints": {
            "POST /predict": "Classify a message",
            "GET /health": "Health check",
            "GET /info": "Model information"
        }
    }), 200

if __name__ == '__main__':
    # Load model on startup
    if load_model_and_vectorizer():
        # Run Flask development server
        app.run(
            host='127.0.0.1',
            port=5000,
            debug=True
        )
    else:
        print("✗ Failed to start server: Model not loaded")
