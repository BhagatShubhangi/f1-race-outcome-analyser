from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

# Load model
with open("models/f1_finish_position_model.pkl", "rb") as f:
    model = pickle.load(f)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()

    features = np.array([[
        data["start_position"],
        data["grid_normalized"],
        data["driver_avg_finish"],
        data["race_difficulty"]
    ]])

    prediction = model.predict(features)[0]

    return jsonify({
        "predicted_finish_position": round(float(prediction), 2)
    })

if __name__ == "__main__":
    app.run(debug=True)
