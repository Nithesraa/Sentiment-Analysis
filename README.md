# 💬 Sentiment Analysis System using Machine Learning

A **multiclass Sentiment Analysis System** that classifies text into **Positive**, **Neutral**, or **Negative** sentiments using **Natural Language Processing (NLP)** and **Machine Learning** techniques.  
The system is trained using **TF-IDF vectorization** and **Logistic Regression**, and deployed as an interactive **Streamlit web application**.

---

## 🚀 Features
- Classifies text into **Positive 😊**, **Neutral 😐**, or **Negative 😠**
- Supports multiclass sentiment analysis
- Clean and modern Streamlit UI
- Real-time sentiment prediction
- Color-coded output:
  - 🟢 Green → Positive
  - 🟡 Yellow → Neutral
  - 🔴 Red → Negative
- Lightweight and fast inference

---

## 🧠 Machine Learning Approach

### 🔹 Data Preprocessing
- Text lowercasing
- Removal of special characters
- Stopword removal using NLTK
- Text normalization

### 🔹 Feature Extraction
- **TF-IDF Vectorization**
- Maximum features: 5000

### 🔹 Model Used
- **Logistic Regression (Multiclass Classification)**

---

## 📊 Model Performance
- Overall accuracy: **~69%**
- Dataset includes **neutral sentiment**, making classification more challenging and realistic
- Balanced performance across all three classes

---

## 📁 Dataset
- Multiclass sentiment dataset
- Labels:
  - `positive`
  - `neutral`
  - `negative`
- Real-world text data with natural ambiguity

---

## 🖥️ Web Application (Streamlit)

The Streamlit app allows users to:
1. Enter any text
2. Click **Analyze Sentiment**
3. Instantly view the sentiment with color-coded feedback
