# VS Code Setup Guide - Smart Scam Message Detector

Complete step-by-step instructions for setting up the project in VS Code.

---

## 📋 Prerequisites

Before starting, ensure you have installed:

1. **VS Code** - [Download](https://code.visualstudio.com/)
2. **Python 3.8+** - [Download](https://www.python.org/downloads/)
3. **Node.js 16+** - [Download](https://nodejs.org/)
4. **Git** - [Download](https://git-scm.com/)

### Verify Installation

Open a terminal (PowerShell or Command Prompt) and run:

```powershell
python --version      # Should show Python 3.8+
node --version        # Should show Node.js 16+
npm --version         # Should show npm 7+
git --version         # Should show git version
```

---

## 🔧 Step 1: Open Project in VS Code

1. Open VS Code
2. **File** → **Open Folder**
3. Navigate to `c:\Users\Sunny mauryavanshi\Projects\ScamMessage`
4. Click **Select Folder**

---

## 🐍 Step 2: Setup Python Environment (Backend)

### 2.1: Open Terminal in VS Code

1. **Terminal** → **New Terminal**
2. Or press `` Ctrl + ` ``

### 2.2: Navigate to Backend

```powershell
cd backend
```

### 2.3: Create Virtual Environment

```powershell
python -m venv venv
```

This creates a folder `venv/` with isolated Python environment.

### 2.4: Activate Virtual Environment

**On Windows (PowerShell)**:
```powershell
venv\Scripts\Activate.ps1
```

**If you get permission error**, run PowerShell as Administrator and try again.

**If still fails**, try Command Prompt instead:
```cmd
venv\Scripts\activate.bat
```

**Expected output**: Your terminal prompt will change to show `(venv)` prefix.

### 2.5: Install Python Dependencies

```powershell
pip install -r requirements.txt
```

This installs:
- Flask
- pandas
- scikit-learn
- joblib
- requests

**Wait for completion** - takes ~2-3 minutes on first install.

### 2.6: Select Python Interpreter in VS Code

1. **Ctrl + Shift + P** → Open Command Palette
2. Type: `Python: Select Interpreter`
3. Choose the one with path `./venv/Scripts/python.exe`

---

## 📊 Step 3: Download Dataset & Train Model

### 3.1: Navigate to Dataset Directory

In the terminal (backend/)):

```powershell
cd ../dataset
```

### 3.2: Download Dataset

```powershell
python download_dataset.py
```

**Expected output**:
```
Downloading dataset from https://raw.githubusercontent.com/...
✓ Dataset downloaded successfully to ...
```

**Note**: If download fails (no internet), it creates a fallback dataset automatically.

### 3.3: Train the Model

```powershell
python train_model.py
```

**Expected output**:
```
============================================================
SCAM MESSAGE DETECTOR - MODEL TRAINING
============================================================

Loading dataset...
✓ Loaded 5574 messages
  - Spam: 747
  - Ham: 4827

Preparing data for training...
✓ Train set: 4459, Test set: 1115

Applying TF-IDF Vectorization...
✓ TF-IDF features created: 3000 features

Training Logistic Regression model...
✓ Model training completed

Model Evaluation:
  - Accuracy:  0.9721
  - Precision: 0.9532
  - Recall:    0.9231
  - F1-Score:  0.9376

✓ Model saved to ...model/scam_detector_model.pkl
✓ Vectorizer saved to ...model/tfidf_vectorizer.pkl

===========================================================
Training completed successfully! ✓
===========================================================
```

### ✅ Model Files Created

Two files are now created in the `model/` folder:
- `scam_detector_model.pkl` - Trained Logistic Regression model
- `tfidf_vectorizer.pkl` - TF-IDF vectorizer

---

## 🚀 Step 4: Start Backend Server

### 4.1: Navigate to Backend

In the terminal:

```powershell
cd ../backend
```

Make sure `(venv)` is shown in prompt. If not, run:
```powershell
venv\Scripts\activate.ps1
```

### 4.2: Run Flask Server

```powershell
python app.py
```

**Expected output**:
```
 * Serving Flask app 'app'
 * Debug mode: on
 * Running on http://127.0.0.1:5000
 * Press CTRL+C to quit
```

**⚠️ Important**: Leave this terminal running! Open a NEW terminal for the frontend.

### 4.3: Test Backend in Browser

Open browser and visit: **http://localhost:5000/info**

You should see JSON with model information.

---

## 🎨 Step 5: Setup Frontend (React)

### 5.1: Open New Terminal in VS Code

**Terminal** → **New Terminal** (or click the + icon)

This opens a new terminal while keeping the Flask server running.

### 5.2: Navigate to Frontend

```powershell
cd frontend
```

### 5.3: Install Node Dependencies

```powershell
npm install
```

This installs:
- React
- Vite
- Tailwind CSS
- Axios

**Wait for completion** - takes ~2-3 minutes on first install.

### 5.4: Start Development Server

```powershell
npm run dev
```

**Expected output**:
```
  VITE v5.0.0  ready in 123 ms

  ➜  Local:   http://localhost:5173/
  ➜  press h to show help
```

---

## 🌐 Step 6: Open Application

1. Visit **http://localhost:5173/** in your browser
2. You should see the Smart Scam Detector interface
3. **Don't close the terminals!** Backend and frontend must keep running.

---

## 🧪 Step 7: Test the Application

### Test with a Safe Message

1. Paste in the textarea:
   ```
   Hey, are you free this weekend? Let's catch up!
   ```
2. Click **🔍 Detect Scam**
3. Result should show:
   - ✅ Safe
   - ~95%+ Confidence

### Test with a Scam Message

1. Paste in the textarea:
   ```
   CONGRATULATIONS! You won $1,000,000! Click here to claim your prize now!
   ```
2. Click **🔍 Detect Scam**
3. Result should show:
   - 🚨 Scam
   - ~95%+ Confidence

---

## 📁 VS Code Extensions (Optional but Recommended)

For better development experience, install these extensions:

1. **Python**
   - Search: `Python`
   - Publisher: Microsoft
   - Provides syntax highlighting, debugging, intellisense

2. **Pylance** (Python language server)
   - Search: `Pylance`
   - Publisher: Microsoft

3. **ES7+ React/Redux/React-Native snippets**
   - Search: `ES7+ React`
   - Publisher: dsznajder.es7-react-js-snippets

4. **Tailwind CSS IntelliSense**
   - Search: `Tailwind CSS IntelliSense`
   - Publisher: bradlc.vscode-tailwindcss

---

## 🔄 Workflow: Running Multiple Terminals

You'll need **2 terminals running simultaneously**:

| Terminal 1 | Terminal 2 |
|-----------|-----------|
| Frontend (http://localhost:5173) | Backend (http://localhost:5000) |
| `npm run dev` | `python app.py` |
| **DO NOT CLOSE** | **DO NOT CLOSE** |

**Layout Suggestion**:
- Split VS Code screen vertically
- Left: Terminal 1 (Frontend)
- Right: Terminal 2 (Backend)
- Browser: Visit http://localhost:5173/

---

## 🐛 Troubleshooting

### Issue: "Command not found: python"

**Solution**: 
1. Check Python is installed: `python --version`
2. If not in PATH, set it in VS Code:
   - **Ctrl + ,** → Settings
   - Search: `Python: Default Interpreter Path`
   - Set to your Python installation path

### Issue: "venv\Scripts\Activate.ps1 cannot be loaded"

**Solution**: Run PowerShell as Administrator

Or use Command Prompt instead:
```cmd
venv\Scripts\activate.bat
python app.py
```

### Issue: "pip: command not found"

**Solution**: Use Python module:
```powershell
python -m pip install -r requirements.txt
```

### Issue: "Port 5000 already in use"

**Solution**: Kill the process using it
```powershell
netstat -ano | findstr :5000           # Find process ID
taskkill /PID <process_id> /F          # Kill it
```

### Issue: "Port 5173 already in use"

**Solution**: Edit `frontend/vite.config.js` and change port:
```javascript
port: 5174,  // Change to different port
```

### Issue: "Cannot connect to server" in frontend

**Solution**:
1. Check Flask is running: Visit http://localhost:5000/health
2. If not, backend terminal might have errors
3. Check for typos in API endpoint in `frontend/src/App.jsx`

### Issue: "No such file or directory: dataset/spam.csv"

**Solution**: Run `python dataset/download_dataset.py` again

### Issue: "Model files not found"

**Solution**: Run `python dataset/train_model.py` to retrain

---

## 📝 Development Tips

### Edit Frontend Code
- Files in `frontend/src/*.jsx`
- Hot reload enabled - changes appear instantly
- No need to restart npm

### Edit Backend Code
- Files in `backend/app.py`
- Flask has debug mode - restart server to apply changes
- Or enable auto-reload in Flask settings

### View Logs
- Backend logs show in `Terminal 2`
- Frontend logs show in `Terminal 1` and Browser DevTools (F12)

### Debug Backend
- Add print statements in Python code
- Logs appear in Terminal 2

---

## ✅ Final Checklist

- [ ] Python virtual environment created and activated
- [ ] `pip install -r requirements.txt` completed
- [ ] `python dataset/download_dataset.py` completed
- [ ] `python dataset/train_model.py` shows successful training
- [ ] Flask server running (`python app.py`)
- [ ] Frontend server running (`npm run dev`)
- [ ] Browser shows interface at http://localhost:5173/
- [ ] Test messages classify correctly

---

## 🎉 Success!

Once all checks pass, your Smart Scam Detector is ready for:
- ✅ Testing
- ✅ Demonstration to faculty
- ✅ Further development

---

## 💡 Next Steps (Optional)

1. **Retrain Model**: Modify `dataset/train_model.py` and retrain with different parameters
2. **Add Features**: Expand `ResultCard.jsx` with more analytics
3. **Deploy**: Follow README.md deployment section
4. **Customize UI**: Modify Tailwind CSS in `frontend/src/App.jsx`

---

**Happy Coding! 🚀**

For detailed information, see [README.md](../README.md)
