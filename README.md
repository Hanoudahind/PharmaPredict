# 💊 PharmaPredict

### Medication Demand Prediction and Restocking Recommendation API

Academic Project — Master in Computer Science and Telecommunications
Supervised by: **Abdelhak Mahmoudi** — Co-Supervised by: **Saad Frihi** & **Yasine Lehmiani**

---

## 📋 Context

Efficient inventory management is a major challenge in the pharmaceutical sector. Poor anticipation of demand can lead to stock shortages, missed sales opportunities, or overstocking of low-turnover products.

**PharmaPredict** is a predictive service that analyzes historical pharmacy sales data to forecast future medication demand and generate restocking recommendations, exposed as a REST API and a simple web interface.

---

## 🎯 Objectives

- Study demand forecasting and stock management problems in the pharmaceutical domain
- Analyze historical sales data to identify consumption patterns
- Develop machine learning models for daily demand prediction
- Generate structured restocking recommendations
- Expose the final system through an API and a web interface

---

## 🛠️ Technologies Used

| Category | Tools |
|---|---|
| Language | Python |
| Data Analysis | Pandas, NumPy |
| Visualization | Matplotlib, Seaborn |
| Machine Learning | XGBoost, scikit-learn (GridSearchCV, TimeSeriesSplit) |
| Model Persistence | Joblib |
| Backend / API | Flask |
| Frontend | HTML, CSS, JavaScript |
| Versioning | Git & GitHub |

---

## 📊 Dataset

The dataset (`salesdaily.csv`) contains **daily pharmacy sales** from 2014 to 2019 for 8 medication categories:

| Code | Category |
|---|---|
| M01AB | Anti-inflammatories (Diclofenac) |
| M01AE | Anti-inflammatories (Ibuprofen) |
| N02BA | Salicylic acid (Aspirin) |
| N02BE | Pyrazolones/Anilides (Paracetamol) |
| N05B | Anxiolytics |
| N05C | Hypnotics and sedatives |
| R03 | Anti-asthmatic drugs |
| R06 | Antihistamines |

---

## 🧠 Machine Learning Pipeline

1. **Data preprocessing** — date parsing, duplicate removal, missing value checks
2. **Exploratory Data Analysis (EDA)** — daily trends, weekly and monthly seasonality per medication
3. **Feature engineering** — temporal features (day of week, day of month, month, year, day of year, is_weekend), lag features (sales from the previous 1 to 7 days), and rolling statistics (7/14/30-day rolling means, 7-day standard deviation)
4. **Model training** — one XGBoost regressor per medication, trained on a chronological 80/20 train-test split
5. **Hyperparameter optimization** — `GridSearchCV` combined with `TimeSeriesSplit` to tune `n_estimators`, `max_depth`, and `learning_rate` while respecting the temporal order of the data
6. **Evaluation** — MAE and RMSE computed on the held-out test set for each medication
7. **Restocking recommendation** — predicted demand for the next day, with a recommended minimum stock level (prediction + 20% safety margin)
8. **Deployment** — models serialized with Joblib and served through a Flask REST API, with a web interface for interactive testing

---

## 📈 Results

Model performance after hyperparameter optimization (Mean Absolute Error, in units/day):

| Medication | MAE | RMSE |
|---|---|---|
| M01AB | 2.23 | 2.85 |
| M01AE | 1.64 | 2.15 |
| N02BA | 1.58 | 2.03 |
| N02BE | 9.15 | 12.14 |
| N05B | 3.16 | 3.98 |
| N05C | 0.83 | 1.14 |
| R03 | 6.11 | 8.81 |
| R06 | 1.65 | 2.20 |

> N02BE (paracetamol) shows the highest error in absolute terms, which is expected given its much higher and more variable sales volume compared to the other categories.

---

## 📁 Project Structure

```
PharmaPredict/
│
├── app.py                          # Flask REST API
├── index.html                      # Web interface for predictions
├── salesdaily.csv                  # Daily sales dataset
├── analyse.ipynb                   # Initial monthly-level exploration & modeling
├── analyse quotidienne (1).ipynb   # Final daily-level pipeline (EDA + ML + optimization)
├── models/                         # Serialized trained models (one per medication)
│   ├── model_M01AB.pkl
│   ├── model_M01AE.pkl
│   ├── model_N02BA.pkl
│   ├── model_N02BE.pkl
│   ├── model_N05B.pkl
│   ├── model_N05C.pkl
│   ├── model_R03.pkl
│   └── model_R06.pkl
└── README.md
```

---

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/Hanoudahind/PharmaPredict.git
cd PharmaPredict
```

### 2. Install dependencies

```bash
pip install pandas numpy matplotlib seaborn scikit-learn xgboost flask joblib
```

### 3. Run the notebook (optional — models are already trained and saved)

Open `analyse quotidienne (1).ipynb` in VS Code or Jupyter and run all cells to reproduce the data analysis, training, and evaluation.

### 4. Run the API

```bash
python app.py
```

### 5. Open the web interface

Go to:

```
http://127.0.0.1:5000
```

---

## 🔌 API Reference

### `POST /predict`

Predicts next-day demand for a given medication and returns a recommended minimum stock level.

**Request body:**

```json
{
  "medicament": "N02BE",
  "dayofweek": 1,
  "dayofmonth": 15,
  "month": 6,
  "year": 2026,
  "dayofyear": 166,
  "is_weekend": 0,
  "lag1": 10,
  "lag2": 12,
  "lag3": 9,
  "lag4": 15,
  "lag5": 8,
  "lag6": 11,
  "lag7": 13,
  "rolling7": 11.14,
  "rolling14": 11.14,
  "rolling30": 11.14,
  "std7": 2.32
}
```

**Response:**

```json
{
  "medicament": "N02BE",
  "ventes_prevues": 15.18,
  "stock_minimum": 18.21
}
```

- `ventes_prevues`: predicted units to be sold the next day
- `stock_minimum`: recommended minimum stock (prediction × 1.2, i.e. +20% safety margin)

---

## 🚀 Possible Improvements

- Extend rolling features to use a true 14/30-day history in the web form (currently approximated from the 7 days provided)
- Add confidence intervals around predictions
- Compare XGBoost against other models (Random Forest, LightGBM, Prophet) per medication
- Deploy the API on a cloud platform with a production-ready WSGI server

---

## 👤 Author

**Hind El Agy**
**Manal El Kabchi**
Master in Computer Science and Telecommunications
Academic Project — Medication Demand Prediction and Restocking Recommendation API
