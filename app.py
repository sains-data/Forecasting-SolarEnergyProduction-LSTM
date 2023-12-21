import streamlit as st
import pandas as pd
import numpy as np
from tensorflow.keras.models import load_model
from sklearn.preprocessing import MinMaxScaler

# Load the pre-trained model
model = load_model('modelDL.h5')

# Load your dataset
data = 'Database.csv'  # Replace with your long file path
df = pd.read_csv(data)

# Load the mean and std values used during training
meanop = df['PV_production'].mean()
stdop = df['PV_production'].std()

# Fit the scaler with the training data
scaler = MinMaxScaler(feature_range=(0, 1))
scaler.fit(df[['DHI', 'DNI', 'GHI', 'Wind_speed', 'Humidity', 'Temperature']])

# Function to preprocess input and make predictions
def predict_pv_production(dhi, dni, ghi, wind_speed, humidity, temperature):

    # Create a DataFrame with the input values
    input_data = pd.DataFrame({
        'DHI': [dhi],
        'DNI': [dni],
        'GHI': [ghi],
        'Wind_speed': [wind_speed],
        'Humidity': [humidity],
        'Temperature': [temperature]
    })

    # Scale the input data using the same scaler used during training
    scaled_input = scaler.transform(input_data)

    # Reshape the input to match the model's expected input shape
    scaled_input = scaled_input.reshape((1, 1, scaled_input.shape[1]))

    # Make the prediction
    prediction = model.predict(scaled_input)

    # Inverse transform the prediction to get the actual PV_production value
    prediction = prediction.ravel()
    prediction = prediction * stdop + meanop

    return prediction[0]

# Streamlit app
def main():
    st.title("PV Production Prediction App")

    # Input form for user input
    dhi = st.number_input("DHI (Direct Horizontal Irradiance)")
    dni = st.number_input("DNI (Direct Normal Irradiance)")
    ghi = st.number_input("GHI (Global Horizontal Irradiance)")
    wind_speed = st.number_input("Wind Speed")
    humidity = st.number_input("Humidity")
    temperature = st.number_input("Temperature")

    # Predict the PV_production
    if st.button("Predict"):
        prediction = predict_pv_production(dhi, dni, ghi, wind_speed, humidity, temperature)
        st.success(f"Predicted PV Production: {prediction:.2f} MW")

if __name__ == "__main__":
    main()