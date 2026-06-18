# PharmaPredict

## Medication Demand Prediction and Restocking Recommendation API

### Project Overview

PharmaPredict is a Machine Learning project developed to predict future medication demand and generate restocking recommendations for pharmacies.

The system uses historical daily sales data to forecast future demand and help improve inventory management.

---

## Technologies Used

* Python
* Pandas
* XGBoost
* Flask
* HTML / CSS / JavaScript
* Git & GitHub

---

## Project Structure

```text
PharmaPredict/
│
├── app.py
├── index.html
├── salesdaily.csv
├── analyse.ipynb
├── analyse quotidienne (1).ipynb
├── models/
│   ├── model_M01AB.pkl
│   ├── model_M01AE.pkl
│   ├── model_N02BA.pkl
│   ├── model_N02BE.pkl
│   ├── model_N05B.pkl
│   ├── model_N05C.pkl
│   ├── model_R03.pkl
│   └── model_R06.pkl
```

---

## Machine Learning Pipeline

1. Data preprocessing
2. Feature engineering
3. XGBoost model training
4. Model serialization using Joblib
5. API development with Flask
6. Web interface integration

---

## Features

* Daily demand prediction
* Multiple medication categories
* Stock recommendation generation
* Interactive web interface
* REST API support

---

## Installation

Install dependencies:

```bash
pip install flask pandas joblib xgboost
```

Run the application:

```bash
python app.py
```

Open your browser:

```text
http://127.0.0.1:5000
```

---

## API Endpoint

### POST /predict

Input:

```json
{
  "medicament": "N02BE",
  "dayofweek": 1,
  "dayofmonth": 15,
  "month": 6,
  "year": 2026,
  "dayofyear": 166,
  "lag1": 10,
  "lag2": 12,
  "lag3": 9,
  "lag4": 15,
  "lag5": 8,
  "lag6": 11,
  "lag7": 13,
  "rolling7": 11.14
}
```

Output:

```json
{
  "medicament": "N02BE",
  "ventes_prevues": 15.18,
  "stock_minimum": 18.21
}
```

---

## Author

Hind El Agy/Z

Master in Computer Science and Telecommunications

Academic Project – Medication Demand Prediction and Restocking Recommendation API
