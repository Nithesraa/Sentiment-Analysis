import pickle
import re
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')

# Load vectorizer
with open("src/tfidf_vectorizer.pkl", "rb") as f:
    tfidf = pickle.load(f)

# Load model
with open("src/sentiment_model.pkl", "rb") as f:
    model = pickle.load(f)


def clean_text(text):
    text = str(text).lower()
    text = re.sub(r'[^a-zA-Z]', ' ', text)
    text = text.split()
    text = [w for w in text if w not in stopwords.words('english')]
    return ' '.join(text)


def predict_sentiment(text):
    cleaned = clean_text(text)
    vectorized = tfidf.transform([cleaned])
    prediction = model.predict(vectorized)[0]

    if prediction == 0:
        return "Negative "
    elif prediction == 1:
        return "Neutral "
    else:
        return "Positive"




