import tensorflow as tf
from keras.layers import Input
from keras.mixed_precision import Policy
import streamlit as st
import gzip
import joblib
import numpy as np

# Set Streamlit theme to dark
st.set_page_config(page_title="Stock Price Prediction", layout="centered", initial_sidebar_state="collapsed")

# Load the model with a custom object scope to handle Input and Policy
with tf.keras.utils.custom_object_scope({'InputLayer': Input, 'DTypePolicy': Policy}):
	model = tf.keras.models.load_model("notebooks/lstm_stock_model.h5", compile=False)


# Load the scaler from the .gz file
with gzip.open("models/google_stock_price_scaler.gz", "rb") as f:
    scaler = joblib.load(f)

st.title("Stock Price Prediction")
# Set Streamlit theme to dark
# Input fields for stock data
open_price = st.number_input("Open Price:", value=0.0)
high_price = st.number_input("High Price:", value=0.0)
low_price = st.number_input("Low Price:", value=0.0)
close_price = st.number_input("Close Price:", value=0.0)
adj_close_price = st.number_input("Adj Close Price:", value=0.0)
volume = st.number_input("Volume:", value=0.0)

# Predict button
if st.button("Predict"):
	try:
		# Prepare input data
		input_data = [[open_price, high_price, low_price, close_price, adj_close_price, volume]]
		scaled_data = scaler.transform(input_data)
		# Reshape the data to match the model's expected input shape
		# Repeat the input data to create a sequence of 60 timesteps
		scaled_data = np.tile(scaled_data, (60, 1)).reshape(1, 60, 6)

		# Make prediction
		prediction = model.predict(scaled_data)
		# Pad the prediction to match the scaler's expected input shape
		padded_prediction = np.zeros((1, 6))
		padded_prediction[0, 0] = prediction[0, 0]
		# Inversing the predicted predicted output using the same scaler
		a = scaler.inverse_transform(padded_prediction)
		st.success(f"Predicted Stock Price: {a[0][0]}")
	except Exception as e:
		st.error(f"Error: {e}")

