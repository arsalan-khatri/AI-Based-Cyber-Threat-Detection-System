import os
import json
import numpy as np
import pandas as pd
import joblib

from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from tensorflow.keras.models import load_model
import math

# 📁 Models directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODELS_DIR = os.path.join(BASE_DIR, 'models')

# ✅ Load scaler, encoder and classifier
scaler = joblib.load(os.path.join(MODELS_DIR, 'scaler.pkl'))
encoder = load_model(os.path.join(MODELS_DIR, 'encoder_model.h5'))
clf = joblib.load(os.path.join(MODELS_DIR, 'xgboost_model.pkl'))

# 📡 API Endpoint for Prediction
@api_view(['GET', 'POST'])
def predict_view(request):
    if request.method == 'GET':
        return Response({'message': 'Please use POST request with input data.'})

    try:
        # 📥 Get JSON data
        input_data = request.data.get('data')
        if input_data is None:
            return Response({'error': 'No input data provided.'})

        # 📊 Convert to DataFrame
        df = pd.DataFrame(input_data)

        # ❌ Drop label columns if accidentally included
        X = df.drop(['label', 'label_binary'], axis=1, errors='ignore')

        # ⚙️ Scale and Encode
        X_scaled = scaler.transform(X)
        X_encoded = encoder.predict(X_scaled)

        # 🤖 Make prediction
        predictions = clf.predict(X_encoded)

        return Response({
            "prediction": predictions.tolist()
        })

    except Exception as e:
        return Response({
            "error": str(e)
        })



@api_view(['GET', 'POST'])
def predict_view1(request):
    if request.method == 'GET':
        return Response({'message': 'Please use POST request with input data.'})

    try:
        input_data = request.data.get('data')
        if input_data is None:
            return Response({'error': 'No input data provided.'})

        # DataFrame
        df = pd.DataFrame(input_data)
        X = df.drop(['label', 'label_binary'], axis=1, errors='ignore')

        # Scale & Encode
        X_scaled = scaler.transform(X)
        X_encoded = encoder.predict(X_scaled)

        # Predictions & Probabilities
        predictions = clf.predict(X_encoded).tolist()
        probabilities = clf.predict_proba(X_encoded)

        # 🔍 Get correct index of 'Attack' class
        attack_class = 1  # or 'Attack' depending on model training
        attack_index = list(clf.classes_).index(attack_class)

        # 🎯 Extract correct attack confidence
        attack_index = list(clf.classes_).index(1)  # 1 for Attack class

        # 🎯 Extract correct attack confidence
        attack_scores = [round(prob[attack_index], 4) for prob in probabilities]

        # String labels
        prediction_labels = ["Attack" if p == 1 else "Benign" for p in predictions]

        # Stats
        total = len(predictions)
        attack_count = predictions.count(1)
        benign_count = predictions.count(0)
        attack_percentage = round((attack_count / total) * 100, 2)

        # Result rows
        result_data = []
        for row, pred_label, score in zip(input_data, prediction_labels, attack_scores):
            row_copy = row.copy()
            row_copy["prediction"] = pred_label
            row_copy["attack_confidence"] = score
            result_data.append(row_copy)

        return Response({
            "total": total,
            "attack_count": attack_count,
            "benign_count": benign_count,
            "attack_percentage": attack_percentage,
            "predictions": predictions,
            "prediction_labels": prediction_labels,
            "attack_confidence_scores": attack_scores,
            "result_data": result_data
        })

    except Exception as e:
        return Response({
            "error": str(e)
        })






# Assuming scaler, encoder, clf (classifier), and attack_index are already defined & loaded

def calculate_entropy(probs):
    probs = np.array(probs)
    probs = probs[probs > 0]  # avoid log(0)
    entropy = -np.sum(probs * np.log2(probs))
    return round(entropy, 4)

def calculate_margin(probs):
    sorted_probs = sorted(probs, reverse=True)
    margin = sorted_probs[0] - sorted_probs[1]
    return round(margin, 4)

@api_view(['GET', 'POST'])
def predict_view2(request):
    if request.method == 'GET':
        return Response({'message': 'Please use POST request with input data.'})

    try:
        input_data = request.data.get('data')
        if input_data is None:
            return Response({'error': 'No input data provided.'})

        # Convert to DataFrame
        df = pd.DataFrame(input_data)
        X = df.drop(['label', 'label_binary'], axis=1, errors='ignore')

        # Scale and Encode
        X_scaled = scaler.transform(X)
        X_encoded = encoder.predict(X_scaled)

        # Predictions & Probabilities
        predictions = clf.predict(X_encoded).tolist()
        probabilities = clf.predict_proba(X_encoded)  # List of [prob_benign, prob_attack]

        result_data = []
        attack_index = 1  # assuming class index 1 is Attack; adjust if different

        attack_count = 0
        benign_count = 0

        for prob in probabilities:
            entropy = calculate_entropy(prob)
            margin = calculate_margin(prob)
            attack_confidence = round(prob[attack_index], 4)
            prediction_label = "Attack" if attack_confidence >= 0.5 else "Benign"

            if prediction_label == "Attack":
                attack_count += 1
            else:
                benign_count += 1

            result_data.append({
                "prediction": prediction_label,
                "attack_confidence": attack_confidence,
                "entropy": entropy,
                "margin": margin
            })

        total = len(predictions)
        attack_percentage = round((attack_count / total) * 100, 2) if total > 0 else 0

        return Response({
            "total": total,
            "attack_count": attack_count,
            "benign_count": benign_count,
            "attack_percentage": attack_percentage,
            "result_data": result_data
        })

    except Exception as e:
        return Response({"error": str(e)})





# 🌐 UI Views
def home(request):
    return render(request, 'home.html')

def prediction(request):
    return render(request, 'pre.html')
