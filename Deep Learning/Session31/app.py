import streamlit as st
import pandas as pd
import joblib

# Load saved model
model = joblib.load("music_genre_model.pkl")

st.set_page_config(
    page_title="Music Genre Classifier",
    page_icon="🎵",
    layout="centered"
)

st.title("🎵 Music Genre Classification")
st.write("Upload a CSV file or enter song features manually to predict the music genre.")

# -----------------------------
# CSV Upload Section
# -----------------------------
st.header("📁 Upload CSV File")

uploaded_file = st.file_uploader(
    "Choose a CSV file",
    type=["csv"]
)

if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)

    predictions = model.predict(df)

    probabilities = model.predict_proba(df)

    confidence = probabilities.max(axis=1)

    df["Predicted Genre"] = predictions
    df["Confidence"] = (confidence * 100).round(2)

    st.success("Prediction Completed!")

    st.dataframe(df)

# -----------------------------
# Manual Prediction Section
# -----------------------------
st.header("🎧 Predict a Single Song")

tempo = st.number_input(
    "Tempo",
    min_value=60,
    max_value=200,
    value=120
)

energy = st.slider(
    "Energy",
    0.0,
    1.0,
    0.5
)

danceability = st.slider(
    "Danceability",
    0.0,
    1.0,
    0.5
)

loudness = st.slider(
    "Loudness",
    -30.0,
    0.0,
    -5.0
)

if st.button("Predict Genre"):

    sample = pd.DataFrame({
        "tempo":[tempo],
        "energy":[energy],
        "danceability":[danceability],
        "loudness":[loudness]
    })


    prediction = model.predict(sample)[0]

    probability = model.predict_proba(sample)

    confidence = probability.max()

    st.success(f"🎼 Predicted Genre: **{prediction}**")

    st.info(f"Confidence Score: **{confidence:.2%}**")
    