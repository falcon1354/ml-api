from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)

model = joblib.load("model/model.pkl")

@app.route("/")
def home():
    return "ML API is running"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()

    age = data["age"]
    salary = data["salary"]

    prediction = model.predict([[age, salary]])

    return jsonify({
        "prediction": int(prediction[0])
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)