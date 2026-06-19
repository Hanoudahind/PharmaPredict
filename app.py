from flask import Flask, request, jsonify, send_file
import joblib
import pandas as pd

app = Flask(__name__)

cols = ['M01AB', 'M01AE', 'N02BA', 'N02BE', 'N05B', 'N05C', 'R03', 'R06']

models = {}
for col in cols:
    models[col] = joblib.load(f"models/model_{col}.pkl")

feature_cols = [
    "dayofweek", "dayofmonth", "month", "year", "dayofyear", "is_weekend",
    "lag1", "lag2", "lag3", "lag4", "lag5", "lag6", "lag7",
    "rolling7", "rolling14", "rolling30", "std7"
]

@app.route("/")
def home():
    return send_file("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()
        medicament = data["medicament"]

        row = {
            "dayofweek": data["dayofweek"],
            "dayofmonth": data["dayofmonth"],
            "month": data["month"],
            "year": data["year"],
            "dayofyear": data["dayofyear"],
            "is_weekend": data["is_weekend"],
            "lag1": data["lag1"],
            "lag2": data["lag2"],
            "lag3": data["lag3"],
            "lag4": data["lag4"],
            "lag5": data["lag5"],
            "lag6": data["lag6"],
            "lag7": data["lag7"],
            "rolling7": data["rolling7"],
            "rolling14": data["rolling14"],
            "rolling30": data["rolling30"],
            "std7": data["std7"]
        }

        X = pd.DataFrame([row], columns=feature_cols)

        prediction = models[medicament].predict(X)[0]
        stock_minimum = prediction * 1.2

        return jsonify({
            "medicament": medicament,
            "ventes_prevues": round(float(prediction), 2),
            "stock_minimum": round(float(stock_minimum), 2)
        })

    except Exception as e:
        return jsonify({"erreur": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)