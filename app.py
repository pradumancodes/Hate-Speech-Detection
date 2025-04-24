from flask import Flask, render_template, request
import pickle
import re
import string
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')
stemmer = nltk.SnowballStemmer("english")
stopword = set(stopwords.words("english"))

# Load model and vectorizer
model = pickle.load(open("model.pkl", "rb"))
cv = pickle.load(open("vectorizer.pkl", "rb"))

# Text Cleaning Function
def clean(text):
    text = str(text).lower()
    text = re.sub(r'\[.*?\]', '', text)
    text = re.sub(r'https?://\S+|www\.\S+', '', text)
    text = re.sub(r'<.*?>+', '', text)
    text = re.sub(r'[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub(r'\n', ' ', text)
    text = re.sub(r'\w*\d\w*', '', text)
    text = [word for word in text.split() if word not in stopword]
    text = " ".join(text)
    text = [stemmer.stem(word) for word in text.split()]
    return " ".join(text)

# Prediction Function
def predict_text(text):
    cleaned = clean(text)
    vectorized = cv.transform([cleaned])
    prediction = model.predict(vectorized)[0]
    return prediction

# Flask App
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    if request.method == "POST":
        text = request.form["text"]
        prediction = predict_text(text)
    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)
