import tensorflow as tf
from tensorflow.keras.models import load_model
from keras.preprocessing.image import img_to_array
import joblib
import numpy as np
from PIL import Image
import io

def preprocess_image(image_data, target_size=(299, 299)):
    img = Image.open(io.BytesIO(image_data))
    img = img.resize(target_size)
    # Convert to RGB mode
    img = img.convert('RGB')
    # Convert to numpy array
    img_array = img_to_array(img)
    # Normalize pixel values to between 0 and 1
    img_array /= 255.
    return img_array

def predict_image(image_data):
    model = load_model('../food101_final_model.keras')
    label_encoder = joblib.load('../image_label_encoder.pkl')

    inception = tf.keras.applications.inception_v3.InceptionV3(include_top=True, input_shape=(299, 299, 3))
    inception = tf.keras.Model([inception.input], [inception.layers[-2].output]) # manually discard prediction layer

    img_array = preprocess_image(image_data)

    img_array = np.expand_dims(img_array, axis=0)

    latent_vector = inception(img_array)
    prediction = model.predict(latent_vector)
    predicted_label = np.argmax(prediction, axis=1)

    predict_label = label_encoder.inverse_transform(predicted_label)
    return predict_label[0]

