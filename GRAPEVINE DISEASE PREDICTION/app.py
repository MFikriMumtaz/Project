# Import necessary libraries
import streamlit as st
import joblib
from PIL import Image
import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt

# Set page title and subtitle
st.title("Grape Disease Prediction")
st.subheader("Insert file to predict")
st.write('The file that you insert must have blank backgound color like white, grey or black background color if not the model will predict poorly')

# Load the class names
with open('class_names.pkl','rb') as file_1:
  class_names = joblib.load(file_1)

# Define the target image size
img_height, img_width = 300, 300

# Function to predict the image
def predict(image):
    # Load the trained model
    model = keras.models.load_model('best_model.h5')

    # Preprocess the image
    img = image.resize((img_height, img_width))
    img_array = keras.preprocessing.image.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0)

    # Make predictions
    predictions = model.predict(img_array)
    score = tf.nn.softmax(predictions[0])

    return class_names[np.argmax(score)], 100 * np.max(score)

# Display file uploader
uploaded_file = st.file_uploader("Choose a file", type=["jpg", "jpeg", "png"])

# Display image and prediction if file is uploaded
if uploaded_file is not None:
    # Check if image has a blank background
    image = Image.open(uploaded_file)
    # Make prediction and display the result
    prediction, confidence = predict(image)
    st.write("The Grape in this image are belongs to {} Classification with a {:.2f}% confidence.".format(prediction, confidence))
    st.image(image, caption='Uploaded Image', use_column_width=True)
   

