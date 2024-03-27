import streamlit as st
import pandas as pd
import predict_img
import make_plot

st.set_option('deprecation.showPyplotGlobalUse', False)

st.title("Gestational HealthSnap")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    image = uploaded_file.read()

    st.image(image, caption='Uploaded Image.', use_column_width=True)

    food = predict_img.predict_image(image)
    st.text(f"The input image is {food}")
    chart = make_plot.makeplot(food)
    st.pyplot(chart)