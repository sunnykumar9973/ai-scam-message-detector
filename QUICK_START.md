# 🚀 Quick Start Guide

**Smart Scam Message Detector** - AI-Powered SMS Classification

---

## ⚡ 30-Second Setup (Windows)

### Option 1: Automatic Setup

```powershell
# Copy and paste in PowerShell (as Administrator):
cd c:\Users\Sunny mauryavanshi\Projects\ScamMessage
.\quick_start.ps1
```

**This will**:
1. ✅ Create Python virtual environment
2. ✅ Install all dependencies
3. ✅ Download dataset & train model
4. ✅ Start backend server
5. ✅ Start frontend server
6. ✅ Open in browser

---

## 📋 Manual Setup (5 minutes)

### Terminal 1: Backend

```powershell
cd c:\Users\Sunny mauryavanshi\Projects\ScamMessage\backend

# Create & activate virtual environment
python -m venv venv
venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt

# Download dataset & train model
cd ../dataset
python download_dataset.py
python train_model.py

# Start server
cd ../backend
python app.py
```

**Console output will show**:
```
✓ Model and vectorizer loaded successfully
 * Running on http://127.0.0.1:5000
```

**Leave this terminal running!**

### Terminal 2: Frontend (New Terminal)

```powershell
cd c:\Users\Sunny mauryavanshi\Projects\ScamMessage\frontend

# Install dependencies
npm install

# Start development server
npm run dev
```

**Console output will show**:
```
VITE v5.0.0  ready in 123 ms
➜  Local:   http://localhost:5173/
```

### Browser

Visit: **http://localhost:5173/**

---

## 📚 File Structure

```
ScamMessage/
│
├── backend/
│   ├── app.py                      # Flask API server (150 lines)
│   ├── requirements.txt             # Python dependencies
│   └── .env.example
│
├── frontend/
│   ├── src/
│   │   ├── App.jsx                 # Main component (150 lines)
│   │   ├── components/
│   │   │   └── ResultCard.jsx      # Result display (80 lines)
│   │   ├── App.css
│   │   ├── index.css
│   │   └── main.jsx
│   ├── index.html
│   ├── package.json
│   ├── vite.config.js
│   ├── tailwind.config.js
│   └── postcss.config.js
│
├── dataset/
│   ├── download_dataset.py         # Download spam data
│   ├── train_model.py              # Training script (200 lines)
│   └── spam.csv                    # (Created after download)
│
├── model/
│   ├── scam_detector_model.pkl     # (Created after training)
│   └── tfidf_vectorizer.pkl        # (Created after training)
│
├── README.md                        # Full documentation
├── PROJECT_SUMMARY.md               # Educational content
├── VSCODE_SETUP.md                  # VS Code instructions
├── quick_start.ps1                  # Automated setup
├── quick_start.bat
└── .gitignore
```

---

## 🧪 Test Messages

### Safe Messages ✅
```
"Hey, are you free this weekend?"
"Let's meet for coffee tomorrow at 3 PM"
"Happy birthday! Hope you have a great day"
```

### Scam Messages 🚨
```
"Congratulations! You won $1,000,000! Click here!"
"FREE iPhone 15! Limited time offer!"
"URGENT: Your account will be closed! Verify here!"
```

---

## 📊 System Requirements

| Component | Requirement |
|-----------|-------------|
| **OS** | Windows 10+ |
| **Python** | 3.8+ |
| **Node.js** | 16+ |
| **RAM** | 2GB minimum |
| **Disk Space** | 500MB |
| **Internet** | For initial setup only |

---

## 🔧 Troubleshooting

### "Cannot connect to server"
- Check backend terminal shows `Running on http://127.0.0.1:5000`
- Refresh browser (Ctrl+R)

### "Port 5000 already in use"
```powershell
netstat -ano | findstr :5000
taskkill /PID <pid_number> /F
```

### "ModuleNotFoundError"
```powershell
# Make sure venv is activated (check for (venv) in prompt)
venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

### "Model files not found"
```powershell
cd dataset
python download_dataset.py
python train_model.py
```

### "npm not found"
- Install Node.js from https://nodejs.org/
- Restart terminal

---

## 🎯 What Does It Do?

```
You paste a message → AI analyzes it → Shows result

Example:
Input:  "Free iPhone! Click here now!!!"
Output: 
  🚨 Scam
  Confidence: 96%
  Safe: 4%
  Scam: 96%
```

---

## 🏗️ Architecture

```
React Frontend ──POST─── Flask Backend ──LOAD──> ML Model
   (Port 5173)     /predict    (Port 5000)      (TF-IDF +
                                                Logistic Regression)
                                                
   Displays          Returns JSON              Trained on
   Results      {"prediction": "Scam",      5,500+ SMS messages
                 "confidence": 96%}
```

---

## 📚 Key Technologies

| Layer | Technology |
|-------|-----------|
| **Frontend** | React 18 + Vite + Tailwind |
| **Backend** | Flask 3.0 + Flask-CORS |
| **ML Model** | scikit-learn (TF-IDF + Logistic Regression) |
| **Deployment** | Local Flask server + Vite dev server |

---

## 📝 Code Metrics

| Metric | Value |
|--------|-------|
| **Total Lines** | ~550 |
| **Frontend Code** | ~230 lines |
| **Backend Code** | ~150 lines |
| **ML Training** | ~200 lines |
| **Model Size** | ~500KB |
| **Training Time** | ~2-3 seconds |
| **Inference Time** | ~5-10ms |

---

## 🎓 Learning Outcomes

After completing this project, you understand:

1. ✅ **Text Vectorization** - TF-IDF algorithm
2. ✅ **Classification** - Logistic Regression
3. ✅ **Model Training** - Using scikit-learn
4. ✅ **Model Serving** - REST API with Flask
5. ✅ **Frontend-Backend Integration** - React + Axios
6. ✅ **Full ML Pipeline** - Data → Training → Serving

---

## 📖 Documentation Files

| File | Purpose |
|------|---------|
| **README.md** | Complete guide + concepts |
| **PROJECT_SUMMARY.md** | Educational content for faculty |
| **VSCODE_SETUP.md** | Step-by-step VS Code setup |
| **This file** | Quick reference |

---

## 🚀 Next Steps

After running successfully:

1. **Understand the Code**
   - Read inline comments in `backend/app.py`
   - Review `frontend/src/App.jsx`
   - Study `dataset/train_model.py`

2. **Experiment with Model**
   - Change hyperparameters in training script
   - Retrain and see performance changes
   - Try different max_features, ngram_range

3. **Enhance Frontend**
   - Add more analytics
   - Improve UI design
   - Add message history

4. **Deploy to Production** (Optional)
   - Use gunicorn for backend
   - Build frontend: `npm run build`
   - Deploy to cloud (Heroku, Vercel, etc.)

---

## 📞 Support

For detailed information:
- **Setup Issues** → [VSCODE_SETUP.md](VSCODE_SETUP.md)
- **How It Works** → [README.md](README.md)
- **ML Concepts** → [PROJECT_SUMMARY.md](PROJECT_SUMMARY.md)

---

**Happy experimenting! 🎉**

---

## CLI Cheat Sheet

```powershell
# Virtual environment
venv\Scripts\Activate.ps1          # Activate
deactivate                          # Deactivate

# Python
python --version                    # Check version
pip install -r requirements.txt    # Install deps
pip freeze                          # List installed

# Node
npm install                         # Install deps
npm run dev                         # Start dev server
npm run build                       # Production build

# Flask
python app.py                       # Start server
# Ctrl+C to stop

# Dataset
python download_dataset.py          # Download
python train_model.py               # Train model

# Testing
curl http://localhost:5000/health   # Check backend
```

---

*Last Updated: August 2026*
