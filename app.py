import pandas as pd
import os
from flask import Flask, request, jsonify

from src.model import Model

app = Flask(__name__)
model = Model()


@app.route("/", methods=["GET"])
def home():
    # At beginning, we load model from MLflow
    return ("OK !", 200)


@app.route("/predict", methods=["POST"])
def predict():
    body = request.get_json()
    df = pd.read_json(body)
    results = [int(x) for x in model.predict(df).flatten()]
    return (jsonify(results), 200)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
