# Streamlit Application

This repository contains:
- Jupyter notebooks for experimentation (`/notebooks`)
- A production-ready Streamlit application (`/streamlit_app`)

## Live Demo
[Deployed on Streamlit Cloud](https://courses-recommender-app.streamlit.app)

## Run Locally

### 1. Clone the repository
```bash
git clone https://github.com/yassine-ramla/courses-recommender.git
cd ui
```

### 2. Create a virtual environment (recommended)
```bash
python -m venv .venv
source .venv/bin/activate   # Linux/Mac
.venv\Scripts\activate      # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the application
```bash
streamlit run Home.py
```