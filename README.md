# Streamlit Application

This repository contains:
- Jupyter notebooks for experimentation (`/notebooks`)
- A production-ready Streamlit application (`/streamlit_app`)

## Live Demo
[Deployed on Streamlit Cloud](https://courses-recommender-app.streamlit.app)

## Run The App Locally

### 1. Clone the repository
```bash
git clone https://github.com/yassine-ramla/courses-recommender.git
cd ui
```
### 2. Create a virtual environment
```bash
python3 -m venv .venv
source .venv/bin/activate   # Linux/Mac
.venv\Scripts\activate      # Windows
```

### 3. Install dependencies
```bash
pip3 install -r requirements.txt
```

### 4. Run the application
```bash
streamlit run Home.py
```

## Run the Notebooks Locally

### 1. Clone the repository
```bash
git clone https://github.com/yassine-ramla/courses-recommender.git
cd notebooks
```
### 2. Create a virtual environment
```bash
python3 -m venv .venv
source .venv/bin/activate   # Linux/Mac
.venv\Scripts\activate      # Windows
```

### 3. Install dependencies
```bash
pip3 install -r requirements.txt
```

### 4. Open the Notebook and select the created env as the Kernel (vscode)

### 5. Click 'Run all cells'