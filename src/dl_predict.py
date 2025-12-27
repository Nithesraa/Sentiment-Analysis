import pickle
import re
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Load tokenizer
with open("src/tokenizer.pkl", "rb") as f:
    tokenizer = pickle.load(f)

# Load DL model
model = load_model("src/sentiment_dl_model.h5")

MAX_LEN = 150

def clean_text(text):
    text = str(text).lower()
    text = re.sub(r'http\S+|www\S+', '', text)
    text = re.sub(r'[^a-zA-Z ]', '', text)
    return text

def predict_sentiment_dl(text):
    cleaned = clean_text(text)
    seq = tokenizer.texts_to_sequences([cleaned])
    padded = pad_sequences(seq, maxlen=MAX_LEN, padding="post")

    probs = model.predict(padded)[0]
    pred_class = np.argmax(probs)
    confidence = round(np.max(probs) * 100, 2)

    if pred_class == 0:
        return "Negative ", confidence
    elif pred_class == 1:
        return "Neutral ", confidence
    else:
        return "Positive ", confidence


# Local test
# if __name__ == "__main__":
#     tests = [
#         "Worst experience ever",
#         "It is okay, nothing special",
#         "Absolutely loved it"
#     ]

#     for t in tests:
#         print(t, "=>", predict_sentiment_dl(t))
