# 💎 Diamond Price Prediction - End-to-End ML Project

## 📌 Overview
This project predicts the price of diamonds based on features like carat, depth, table, dimensions, cut, color, and clarity.

It is a complete **end-to-end Machine Learning project** including data ingestion, transformation, model training, evaluation, and deployment using Flask.

---

## 🚀 Features
- End-to-End ML Pipeline
- Data Ingestion & Preprocessing
- Feature Engineering using Scikit-learn Pipelines
- Model Training & Evaluation
- MLflow for experiment tracking
- Flask Web Application for prediction
- Clean UI using HTML & CSS

---

## 🧠 Models Used
- Linear Regression  
- Lasso Regression  
- Ridge Regression  
- ElasticNet Regression  

---

## 📊 Tech Stack
- Python  
- Pandas  
- NumPy  
- Scikit-learn  
- MLflow  
- Flask  
- HTML  
- CSS  

---

## 📁 Project Structure
Diamond Price Prediction/
│── src/
│ ├── components/
│ ├── pipelines/
│ ├── utils/
│ ├── exception.py
│ ├── logger.py
│
│── templates/
│ ├── form.html
│ ├── result.html
│
│── static/
│ ├── style.css
│
│── app.py
│── requirements.txt
│── setup.py
│── .gitignore


---

## ⚙️ Installation

### 1️⃣ Clone the repository
```bash
git clone https://github.com/Keerthivardhan1507/Diamond-Price-Prediction.git
cd Diamond-Price-Prediction

2️⃣ Create environment

```bash
conda create -n diamond python=3.10
conda activate diamond

3️⃣ Install dependencies

```bash
pip install -r requirements.txt

▶️ Run the Project
🔹 Run Training Pipeline
```bash
python -m src.pipelines.training_pipeline

🔹 Run Flask App

python app.py
👉 Open browser:
http://127.0.0.1:8080/

📸 Output

The application takes user input and predicts the diamond price in real-time.

c:\Users\KEERTHI VARDHAN\OneDrive\Pictures\Diamond.png

📈 MLflow Tracking

mlflow ui

mlflow ui

👉 Open:
http://localhost:5000

💡 Key Learnings
Built modular ML pipelines
Learned model deployment using Flask
Understood experiment tracking using MLflow
Implemented production-ready project structure
🔗 GitHub Repository

https://github.com/Keerthivardhan1507/Diamond-Price-Prediction

👨‍💻 Author

Keerthi Vardhan Naidu

---

# 🚀 Final Step

After pasting:

```bash
git add README.md
git commit -m "Added professional README"
git push
