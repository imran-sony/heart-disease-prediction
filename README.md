# ❤️ Heart Disease Prediction API 

A simple FastAPI application that serves a machine learning model for predicting the likelihood of heart disease based on clinical features.  
The model is trained using scikit-learn’s RandomForestClassifier and deployed with FastAPI + Uvicorn in Docker.

## 📁 Project Structure 

├── app/  
│   ├── main.py          # FastAPI application  
│   └── schemas.py       # Pydantic data model  
├── data/  
│   └── heart.csv        # Dataset  
├── model/  
│   └── heart_model.joblib  # Trained ML model (generated)  
├── train_model.py       # Script to train and save model  
├── requirements.txt     # Python dependencies  
├── Dockerfile           # Docker build instructions  
└── docker-compose.yml   # Docker Compose configuration  

## 🧠 Model Training

To train the model locally:
```
python train_model.py
```
This will:

Load data/heart.csv

Train a RandomForestClassifier

Save the trained model to model/heart_model.joblib

Print the model’s accuracy score

## ⚙️ API Overview  
### Endpoints    
GET	/health	-> Health check for the API service  
GET	/info	-> Returns model info and feature names  
POST	/predict	-> Predicts heart disease from input  

## 🧩 Run Locally (without Docker)

### Create and activate a virtual environment:
```
python -m venv .venv 
.venv\Scripts\activate
```

### Install dependencies:
```
pip install -r requirements.txt
```

## 🐳 Run with Docker
Build and run using Docker Compose:  
```
docker compose build --no-cache  
docker compose up  
```

### Start the API:
```
uvicorn app.main:app --reload
```

### Open your browser:
👉 http://127.0.0.1:8000/docs
