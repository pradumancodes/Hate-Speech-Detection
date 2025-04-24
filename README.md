# 🧠 Hate Speech Detection Model

A Machine Learning-based web app to detect **Hate Speech**, **Offensive Language**, or **Neutral Content** from user-inputted text.  
Built using Python, scikit-learn, Flask, and a Twitter hate speech dataset.

---

## 📂 Dataset

- **Source:** [Twitter Hate Speech Dataset on Kaggle](https://www.kaggle.com/datasets/lakshmi25npathi/twitter-sentiment-analysis-hatred-speech)
- **Classes:**
  - `0` → Hate Speech
  - `1` → Offensive Language
  - `2` → No Hate & Offensive Speech

We mapped these to:
- **Hate Speech**
- **Offensive Language**
- **Neutral**

---

## 🛠️ Tools & Libraries

- Python
- scikit-learn
- NLTK
- Flask
- Bootstrap (for UI)
- Pandas, NumPy

---

## ⚙️ Model Building Approach

1. **Preprocessing**
   - Lowercasing, URL and punctuation removal
   - Stopword removal
   - Stemming using NLTK

2. **Feature Extraction**
   - CountVectorizer (Bag-of-Words)

3. **Model Used**
   - Logistic Regression (trained with `scikit-learn`)

4. **Evaluation Metrics**

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Classification Report:
               precision    recall  f1-score   support

   Hate Speech       0.47      0.23      0.31       465
       Neutral       0.82      0.86      0.84      1379

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![Screenshot 2025-04-24 192154](https://github.com/user-attachments/assets/401a0318-3836-4b8c-940b-88b1742fc157)

📁 Project Structure

hate-speech-detector/
├── app.py
├── model.pkl
├── vectorizer.pkl
├── twitter_data.csv
├── templates/
│   └── index.html
├── screenshot.png
├── README.md

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

📌 Deliverables
✅ Source Code: app.py, model files, etc.

✅ Sample Dataset: twitter_data.csv

✅ Trained Model: model.pkl, vectorizer.pkl

✅ Web Interface: Flask

✅ README with setup + approach

✅ Screenshot: included

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

🙋‍♂️ Author
Name: Praduman Sharma

Email: praduman0571@gmail.com

GitHub: github.com/pradumancodes
