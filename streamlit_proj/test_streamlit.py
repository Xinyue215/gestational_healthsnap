import streamlit as st
import pandas as pd
import predict_img
import make_plot
import pickle

with open('food_dict.pkl', 'rb') as pickle_file:
    food_dict = pickle.load(pickle_file)

st.set_option('deprecation.showPyplotGlobalUse', False)

st.title("Gestational HealthSnap")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    image = uploaded_file.read()

    st.image(image, caption='Uploaded Image.', use_column_width=True)

    food = predict_img.predict_image(image)
    predicted_food = food_dict[food]
    
    # Provide a dropdown menu for the user to select "Yes" or "No"
    confirmation = st.selectbox(f"Is the predicted category: {predicted_food} correct?", ["Please Select","Yes", "No"])

    if confirmation == "No":
        # Provide a dropdown menu to select the correct category
        selected_food = st.selectbox("Select the correct category:", ["Please Select"] + list(food_dict.values()))
        
        if selected_food != "Please Select":
            food = [key for key, value in food_dict.items() if value == selected_food][0]
            st.text(f"The input image is {food_dict[food]}")
            chart = make_plot.makeplot(food)
            st.pyplot(chart)
        
    elif confirmation == "Yes":
        food = [key for key, value in food_dict.items() if value == predicted_food][0]

        st.text(f"The input image is {food_dict[food]}")
        chart = make_plot.makeplot(food)
        st.pyplot(chart)


