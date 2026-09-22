"""
Quick test script to call the trained model and the same rule-logic used in the API.
Run with backend venv python to confirm behavior without restarting Flask.
"""
import joblib
import os
import re

MODEL_DIR = os.path.join(os.path.dirname(__file__), '..', 'model')
MODEL_FILE = os.path.join(MODEL_DIR, 'scam_detector_model.pkl')
VECTORIZER_FILE = os.path.join(MODEL_DIR, 'tfidf_vectorizer.pkl')

model = joblib.load(MODEL_FILE)
vectorizer = joblib.load(VECTORIZER_FILE)

message = "Congratulations! You won £1,000. Click http://claim-prize.example now to collect — valid 24 hours."

# Vectorize
msg_tfidf = vectorizer.transform([message])
probs = model.predict_proba(msg_tfidf)[0].astype(float)

# Rule booster (same logic as API)
rule_score = 0.0
if re.search(r'https?://\S+|www\.\S+', message, flags=re.IGNORECASE):
    rule_score += 0.30

spam_keywords = ['congrat', 'won', 'prize', 'claim', 'free', 'urgent', 'verify', 'click', 'winner', 'selected', 'cash']
found = 0
low_msg = message.lower()
for kw in spam_keywords:
    if kw in low_msg:
        found += 1
rule_score += min(0.08 * found, 0.30)

scam_prob = float(probs[1]) + rule_score
safe_prob = float(probs[0])
if scam_prob + safe_prob > 0:
    total = scam_prob + safe_prob
    scam_prob = scam_prob / total
    safe_prob = safe_prob / total

print('Model raw probs -> safe: {:.2f}, scam: {:.2f}'.format(float(probs[0]), float(probs[1])))
print('After rule boost -> safe: {:.2f}, scam: {:.2f}'.format(safe_prob, scam_prob))
print('Final prediction:', 'SCAM' if scam_prob >= 0.5 else 'SAFE')
