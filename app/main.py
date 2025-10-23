from fastapi import FastAPI
from app.schemas import HeartData
import joblib
import os

# Load model
MODEL_PATH = os.path.join("model", "heart_model.joblib")
model = joblib.load(MODEL_PATH)

# Feature list
FEATURES = ["age","sex","cp","trestbps","chol","fbs","restecg",
            "thalach","exang","oldpeak","slope","ca","thal"]

app = FastAPI(title="Heart Disease Prediction API")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/info")
def info():
    return {"model": type(model).__name__,
            "features": FEATURES}

@app.post("/predict")
def predict(data: HeartData):
    input_data = [[
        data.age, data.sex, data.cp, data.trestbps, data.chol,
        data.fbs, data.restecg, data.thalach, data.exang,
        data.oldpeak, data.slope, data.ca, data.thal
    ]]
    prediction = model.predict(input_data)[0]
    return {"heart_disease": bool(prediction)}