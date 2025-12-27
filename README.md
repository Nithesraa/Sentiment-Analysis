# 🧠 Sentiment Analysis using Deep Learning (BiLSTM)

A **multiclass Sentiment Analysis System** built using **Deep Learning (Bidirectional LSTM)** to classify text into **Positive**, **Neutral**, or **Negative** sentiments.  
The project demonstrates an end-to-end **NLP deep learning pipeline**, from preprocessing and model training to deployment using **Streamlit**.

---

## 🚀 Features
- Multiclass sentiment classification:
  - 🟢 Positive
  - 🟡 Neutral
  - 🔴 Negative
- Deep Learning model using **Bidirectional LSTM (RNN-based)**
- Handles class imbalance using **class weights**
- Confidence score displayed for predictions
- Clean and interactive **Streamlit web interface**
- Real-time sentiment analysis

---

## 🧠 Deep Learning Approach

### 🔹 Model Architecture
- Tokenizer + Padding
- Embedding Layer
- **Bidirectional LSTM**
- Fully Connected Dense Layers
- Softmax output layer (3 classes)

### 🔹 Why BiLSTM?
- Captures **context from both past and future words**
- Handles negations better than traditional ML models
- Suitable for NLP tasks like sentiment analysis

---

## 📊 Model Performance
- Task: **Multiclass Sentiment Classification**
- Classes: Positive / Neutral / Negative
- Test Accuracy: **~63%**
- Improved significantly from baseline after:
  - Increasing epochs
  - Using Bidirectional LSTM
  - Applying class weight balancing

> Note: Neutral sentiment overlaps with positive/negative, making the task more challenging and realistic.

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
3. View predicted sentiment with confidence score
4. Get color-coded feedback for clarity
