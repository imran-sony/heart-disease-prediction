# ❤️ Heart Disease Prediction API 

A simple FastAPI application that serves a machine learning model for predicting the likelihood of heart disease based on clinical features. The model is trained using scikit-learn’s RandomForestClassifier and deployed with FastAPI + Uvicorn in Docker.

## 🎯 Features
1. age
2. sex
3. chest pain type (4 values)
4. resting blood pressure
5. serum cholestoral in mg/dl
6. fasting blood sugar > 120 mg/dl
7. resting electrocardiographic results (values 0,1,2)
8. maximum heart rate achieved
9. exercise induced angina
10. oldpeak = ST depression induced by exercise relative to rest
11. the slope of the peak exercise ST segment
12. number of major vessels (0-3) colored by flourosopy
13. thal: 0 = normal; 1 = fixed defect; 2 = reversable defect

**Target:** Heart disease in the patient: 0 = no disease and 1 = disease

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

Train the model locally
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

## 🧩 Run Locally

### Create and activate a virtual environment
```
python -m venv .venv 
.venv\Scripts\activate
```

### Install dependencies
```
pip install -r requirements.txt
```

## 🐳 Run with Docker
Build and run using Docker Compose:  
```
docker compose build --no-cache  
docker compose up  
```

## 🧾 Start the API
```
uvicorn app.main:app --reload
```

### Open your browser:
👉 http://127.0.0.1:8000/docs
