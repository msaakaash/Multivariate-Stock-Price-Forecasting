import numpy as np
from fastapi import FastAPI
from pydantic import BaseModel
import tensorflow as tf

app = FastAPI()

# Load the trained model
model = tf.keras.models.load_model("C:/Users/Aniketha Prasad/Documents/NNDL/Multivariate-Stock-Price-Forecasting/notebooks/lstm_stock_model.h5")

# Define request format
class InputData(BaseModel):
    input_data: list  # Expecting a list of lists (60, 6)

@app.post("/predict")
def predict(data: InputData):
    input_array = np.array(data.input_data, dtype=np.float32)
    
    # Reshape to (1, 60, 6) before passing to LSTM
    if input_array.shape == (60, 6):
        input_array = input_array.reshape(1, 60, 6)
    else:
        return {"error": "Invalid input shape. Expected (60, 6)."}

    prediction = model.predict(input_array)
    
    return {"prediction": prediction.tolist()}

@app.get("/")  # This defines the root URL
def read_root():
    return {"message": "API is running successfully!"}
