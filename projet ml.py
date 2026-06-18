from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

# Charger tous les modèles
cols = ['M01AB', 'M01AE', 'N02BA', 'N02BE', 'N05B', 'N05C', 'R03', 'R06']
models = {}
for col in cols:
    models[col] = joblib.load(f'models/model_{col}.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    medicament = data['medicament']
    month = data['month']
    year = data['year']
    lag1 = data['lag1']
    lag2 = data['lag2']
    lag3 = data['lag3']
    
    X = pd.DataFrame([[month, year, lag1, lag2, lag3]],
                     columns=['month', 'year', 'lag1', 'lag2', 'lag3'])
    
    prediction = models[medicament].predict(X)[0]
    seuil = prediction * 1.2
    
    return jsonify({
        'medicament': medicament,
        'ventes_prevues': round(prediction, 2),
        'stock_minimum': round(seuil, 2)
    })

@app.route('/', methods=['GET'])
def home():
    return jsonify({'message': 'API Pharmacie opérationnelle ✅'})

if __name__ == '__main__':
    app.run(debug=True)