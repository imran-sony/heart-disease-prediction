# ❤️ Heart Disease Prediction API

A simple FastAPI application that serves a machine learning model for predicting the likelihood of heart disease based on clinical features.
The model is trained using scikit-learn’s RandomForestClassifier and deployed with FastAPI + Uvicorn in Docker.

# 📁 Project Structure

├── app/
│   ├── main.py          # FastAPI application
│   └── schemas.py       # Pydantic data model
├── data/
│   └── heart.csv        # Dataset (not included in repo)
├── model/
│   └── heart_model.joblib  # Trained ML model (generated)
├── train_model.py       # Script to train and save model
├── requirements.txt     # Python dependencies
├── Dockerfile           # Docker build instructions
└── docker-compose.yml   # Docker Compose configuration
