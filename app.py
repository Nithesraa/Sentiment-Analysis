import streamlit as st
from src.dl_predict import predict_sentiment_dl

st.set_page_config(
    page_title="Sentiment Analysis (Deep Learning)",
    page_icon="🧠",
    layout="centered"
)

st.title("🧠 Sentiment Analysis using Deep Learning (BiLSTM)")
st.write(
    "Analyze text sentiment using a **Bidirectional LSTM deep learning model**.\n\n"
    "Outputs: **Positive**, **Neutral**, or **Negative**"
)

user_input = st.text_area("Enter text", height=150)

if st.button("Analyze Sentiment"):
    if user_input.strip() == "":
        st.warning("⚠️ Please enter some text")
    else:
        label, confidence = predict_sentiment_dl(user_input)

        if "Negative" in label:
            st.error(f"🔴 {label}\n\nConfidence: {confidence}%")
        elif "Neutral" in label:
            st.warning(f"🟡 {label}\n\nConfidence: {confidence}%")
        else:
            st.success(f"🟢 {label}\n\nConfidence: {confidence}%")

with st.expander(" Model Information"):
    st.write("""
    - Model: Bidirectional LSTM (RNN)
    - Embedding-based Deep Learning
    - Handles class imbalance using class weights
    - Trained on multiclass sentiment dataset
    """)
