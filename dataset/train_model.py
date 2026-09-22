"""
Scam Message Detector - Model Training Script
Trains a Logistic Regression model with TF-IDF vectorization
to detect spam/scam messages.

Why TF-IDF?
- TF-IDF (Term Frequency-Inverse Document Frequency) converts raw text
  into numerical features that ML models can understand.
- It weights important words higher and common words lower.
- Efficient and interpretable for text classification.

Why Logistic Regression?
- Simple yet effective for binary classification (Spam vs. Ham).
- Fast to train and predict.
- Provides confidence scores (probabilities).
- Easy to explain for educational purposes.
"""

import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import joblib
import os

# Paths
DATASET_PATH = os.path.join(os.path.dirname(__file__), "spam.csv")
MODEL_DIR = os.path.join(os.path.dirname(__file__), "..", "model")
MODEL_FILE = os.path.join(MODEL_DIR, "scam_detector_model.pkl")
VECTORIZER_FILE = os.path.join(MODEL_DIR, "tfidf_vectorizer.pkl")

def load_data():
    """Load and prepare the dataset"""
    print("Loading dataset...")
    
    df = pd.read_csv(DATASET_PATH)
    
    # Verify dataset has required columns
    if df.shape[1] < 2:
        raise ValueError("Dataset should have at least 2 columns: label and message")
    
    # Use first column as label, second as message
    df.columns = ['label', 'message']
    
    # Convert labels: 'spam' -> 1, 'ham' -> 0
    df['label'] = df['label'].map({'spam': 1, 'ham': 0})
    
    # Remove any null values
    df = df.dropna()
    
    print(f"✓ Loaded {len(df)} messages")
    print(f"  - Spam: {(df['label'] == 1).sum()}")
    print(f"  - Ham: {(df['label'] == 0).sum()}")
    
    return df

def preprocess_text(text):
    """
    Preprocess text for better ML performance
    - Convert to lowercase
    - Remove extra whitespace
    """
    # Already lowercase for simplicity, TF-IDF will handle it
    return str(text).strip()

def train_model(df):
    """
    Train the spam detection model
    1. Split data into train/test sets
    2. Apply TF-IDF vectorization
    3. Train Logistic Regression
    4. Evaluate performance
    """
    print("\nPreparing data for training...")
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        df['message'], df['label'],
        test_size=0.2,
        random_state=42,
        stratify=df['label']
    )
    
    print(f"✓ Train set: {len(X_train)}, Test set: {len(X_test)}")
    
    # Step 1: TF-IDF Vectorization
    print("\nApplying TF-IDF Vectorization...")
    vectorizer = TfidfVectorizer(
        max_features=3000,      # Use top 3000 features
        stop_words='english',   # Remove common English words
        lowercase=True,
        ngram_range=(1, 2)      # Use unigrams and bigrams
    )
    
    X_train_tfidf = vectorizer.fit_transform(X_train)
    X_test_tfidf = vectorizer.transform(X_test)
    
    print(f"✓ TF-IDF features created: {X_train_tfidf.shape[1]} features")
    
    # Step 2: Train Logistic Regression
    print("\nTraining Logistic Regression model...")
    model = LogisticRegression(
        max_iter=1000,
        random_state=42,
        solver='lbfgs',
        class_weight='balanced'
    )
    
    model.fit(X_train_tfidf, y_train)
    print("✓ Model training completed")
    
    # Step 3: Evaluate model
    print("\nModel Evaluation:")
    y_pred = model.predict(X_test_tfidf)
    
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)
    
    print(f"  - Accuracy:  {accuracy:.4f}")
    print(f"  - Precision: {precision:.4f}")
    print(f"  - Recall:    {recall:.4f}")
    print(f"  - F1-Score:  {f1:.4f}")
    
    return model, vectorizer

def save_model(model, vectorizer):
    """Save trained model and vectorizer using joblib"""
    os.makedirs(MODEL_DIR, exist_ok=True)
    
    # Save model
    joblib.dump(model, MODEL_FILE)
    print(f"\n✓ Model saved to {MODEL_FILE}")
    
    # Save vectorizer
    joblib.dump(vectorizer, VECTORIZER_FILE)
    print(f"✓ Vectorizer saved to {VECTORIZER_FILE}")

def main():
    """Main training pipeline"""
    print("=" * 60)
    print("SCAM MESSAGE DETECTOR - MODEL TRAINING")
    print("=" * 60)
    
    try:
        # Load data
        df = load_data()
        
        # Train model
        model, vectorizer = train_model(df)
        
        # Save model
        save_model(model, vectorizer)
        
        print("\n" + "=" * 60)
        print("Training completed successfully! ✓")
        print("=" * 60)
        
    except FileNotFoundError:
        print(f"\n✗ Error: Dataset not found at {DATASET_PATH}")
        print("Please run: python dataset/download_dataset.py")
    except Exception as e:
        print(f"\n✗ Error during training: {e}")

if __name__ == "__main__":
    main()
