import joblib
import numpy as np
import os
# Load trained ML model
# Get the directory of this file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Path to the saved model
MODEL_PATH = os.path.join(BASE_DIR, "cybersickness_model.pkl")

# Load trained ML model
model = None

def get_model():
    global model
    if model is None:
        model = joblib.load(MODEL_PATH)
    return model



def preprocess(features):

    gender = features["gender"]
    gad_score = features["gad_score"]
    task_condition = features["task_condition"]

    # One-hot encoding for task condition
    cond_2 = 1 if task_condition == "0-back" else 0
    cond_3 = 1 if task_condition == "2-back" else 0

    return [gender, gad_score, cond_2, cond_3]


def predict(features: dict):

    X = preprocess(features)

    prediction = get_model().predict([X])

    return int(prediction[0])
