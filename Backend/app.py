from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
import numpy as np
import pandas as pd

app = Flask(__name__)
CORS(app)

# Load the trained model
with open("iris_model.pkl", "rb") as f:
    model = pickle.load(f)

# Load the trained StandardScaler
with open("scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

# Define feature names (Ensure they match training)
feature_names = ["sepal length (cm)", "sepal width (cm)", "petal length (cm)", "petal width (cm)"]

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        features = np.array(data["features"]).reshape(1, -1)

        # Convert to DataFrame with feature names
        features_df = pd.DataFrame(features, columns=feature_names)

        # Apply the same StandardScaler transformation
        scaled_features = scaler.transform(features_df)

        # Make prediction using the scaled input
        prediction = model.predict(scaled_features)[0]

        return jsonify({"prediction": prediction})
    except Exception as e:
        return jsonify({"error": str(e)})

@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "Flask Backend is Running!"})


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000) 
