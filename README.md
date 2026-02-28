# 🏎️ F1 Race Outcome & Strategy Analyzer

An end-to-end Machine Learning project that analyzes historical Formula 1 race data to predict race finishing positions using a Random Forest Regressor.

The project covers the full ML lifecycle — from data preprocessing and exploratory analysis to model training, evaluation, and deployment using Flask with a simple interactive web interface.


## 🚀 Project Overview

This project uses historical F1 race data to:
- Clean and preprocess raw race datasets
- Perform exploratory data analysis (EDA)
- Engineer meaningful race features
- Train a Random Forest regression model
- Evaluate model performance
- Deploy the trained model using Flask
- Provide predictions through a simple frontend interface


## 🧠 Machine Learning Workflow

1. Data Cleaning & Preprocessing
2. Exploratory Data Analysis (EDA)
3. Feature Engineering
4. Model Selection (Random Forest Regressor)
5. Model Training
6. Model Evaluation (Error Analysis & Metrics)
7. Model Deployment via Flask


## 🛠️ Tech Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib / Seaborn
- Flask
- HTML / CSS / JavaScript


## 📂 Project Structure

```
F1_RACE_STRATEGY_ML/
│
├── data/                # Raw CSV datasets
├── notebooks/           # Jupyter notebook (analysis & model training)
├── models/              # Trained model file (excluded from GitHub)
├── static/              # CSS & JavaScript files
├── templates/           # HTML frontend
├── app.py               # Flask backend application
├── requirements.txt     # Project dependencies
└── README.md
```


## 🔍 How to Run the Project

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/<your-username>/<your-repo-name>.git
cd F1_RACE_STRATEGY_ML
```



### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```


### 3️⃣ Run the Flask Application

```bash
python app.py
```



### 4️⃣ Open in Browser

```
http://127.0.0.1:5000/
```

You can now enter race parameters and receive predicted finishing positions.



## 📊 Key Insights

- Starting grid position significantly influences final race results.
- Historical driver performance impacts race outcomes.
- Random Forest performs well due to its ability to capture nonlinear feature relationships.
- Error analysis reveals higher variance in unpredictable race conditions.



## 📌 Future Improvements

- Compare performance with Gradient Boosting / XGBoost
- Deploy the app publicly (Render / Railway)
- Add prediction confidence intervals
- Integrate real-time F1 API data
- Improve UI with advanced visualizations



## 🎯 Project Goals

This project was built to:
- Practice end-to-end ML development
- Understand regression modeling in sports analytics
- Gain experience deploying ML models using Flask
- Build a production-style ML workflow

