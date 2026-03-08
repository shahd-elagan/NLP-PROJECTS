import streamlit as st
from PIL import Image
import pandas as pd

from imagecaption import generate_caption
from classifier import classify_text
from database import save_to_db, load_db


st.title("Cellula AI Content Analyzer")

option = st.sidebar.selectbox(
    "Choose input type",
    ["Text Classification", "Image Caption + Classification", "View Database"]
)

if option == "Text Classification":

    st.header("Enter Text")

    user_text = st.text_area("Write your text here")

    if st.button("Classify"):

        if user_text:

            label, score = classify_text(user_text)

            st.success(f"Classification: {label}")
            st.write(f"Confidence: {score:.2f}")

            save_to_db(user_text, label)


elif option == "Image Caption + Classification":

    st.header("Upload Image")

    uploaded_file = st.file_uploader("Upload image", type=["png", "jpg", "jpeg"])

    if uploaded_file:

        image = Image.open(uploaded_file)

        st.image(image, caption="Uploaded Image")

        caption = generate_caption(image)

        st.write("Generated Caption:")
        st.success(caption)

        label, score = classify_text(caption)

        st.write("Classification Result:")
        st.success(label)

        save_to_db(caption, label)


 
elif option == "View Database":

    st.header("Stored Data")

    df = load_db()

    st.dataframe(df)