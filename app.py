import streamlit as st
from src.predict import predict_sentiment

st.set_page_config(
    page_title="Sentiment Analysis System",
    page_icon="💬",
    layout="centered"
)

st.title("💬 Sentiment Analysis System")
st.write("Analyze text sentiment as **Positive**, **Neutral**, or **Negative**.")

user_input = st.text_area("Enter your text here", height=150)

if st.button("Analyze Sentiment"):
    if user_input.strip() == "":
        st.warning("⚠️ Please enter some text")
    else:
        result = predict_sentiment(user_input)

        if "Negative" in result:
            st.error(f"Result: {result}")
        elif "Neutral" in result:
            st.warning(f"Result: {result}")
        else:
            st.success(f"Result: {result}")