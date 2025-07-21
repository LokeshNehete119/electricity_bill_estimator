# ⚡ Electricity Bill Prediction - Machine Learning Project

Predicting monthly electricity bills based on appliance usage daily hours using regression-based machine learning models.

Accurately forecasting electricity bills is crucial for energy planning and saving costs. This project aims to build a predictive model that estimates the monthly electricity bill based on the usage hours of household appliances fan, refrigerator, television, air conditioner, monitor, taking into account the tariff rate.


## 📊 Dataset

The dataset was sourced from **Kaggle** and includes:
- Appliance-wise usage hours (/day)
- Month of the year
- Monthly electricity tariff rate (₹/unit)
- Final electricity bill (₹)


## 📈 Models Implemented

We experimented with various supervised-learning regression models:
- Linear Regression
- Random Forest Regressor 
- Gradient Boosting Regressor

Among these Gradient Boosting Regressor model performed the best with a R² score of 0.5939

Hyperparameter tuning was applied for Gradient Boosting Regressor model using:
- **GridSearchCV**
- **RandomizedSearchCV**

The tuned Gradient Boosting Regressor model with GridSearchCV ouperformed the untuned one with best R² score of 0.59476


## 🖥️ Gradio Web App

I built a simple interactive UI using **Gradio** where users can enter their appliance usage and instantly get an estimated electricity bill.


## 📌 Technologies Used

- Python
- NumPy, Pandas, Matplotlib, Seaborn
- Scikit-learn
- Gradio

