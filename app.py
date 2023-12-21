import streamlit as st
import pandas as pd
import numpy as np
from tensorflow.keras.models import load_model
from sklearn.preprocessing import MinMaxScaler
import pickle

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

# Function to load data from pickle file
def load_data_from_pickle(file_path):
    with open(file_path, 'rb') as file:
        data = pickle.load(file)
    return data

# Streamlit app
def main():
    st.title("PV Production Prediction App")

    # Option to choose input type
    input_type = st.radio("Choose Input Type", ["Manual Input", "Load from Pickle"])

    if input_type == "Manual Input":
        # Input form for user input
        dhi = st.number_input("DHI (Direct Horizontal Irradiance) (W/m2)")
        dni = st.number_input("DNI (Direct Normal Irradiance) (W/m2)")
        ghi = st.number_input("GHI (Global Horizontal Irradiance) (W/m2)")
        wind_speed = st.number_input("Wind Speed (m/s)")
        humidity = st.number_input("Humidity (%)")
        temperature = st.number_input("Temperature (degress)")
    else:
        # Input form for loading data from pickle
        pickle_file = st.file_uploader("Upload Pickle File", type=["pickle"])
        if pickle_file is not None:
            loaded_data = load_data_from_pickle(pickle_file)
            
            # Display loaded data
            st.write("Loaded Data:")
            st.write(loaded_data)

            # Extract values from loaded data (modify as needed based on your pickle structure)
            dhi = loaded_data['DHI']
            dni = loaded_data['DNI']
            ghi = loaded_data['GHI']
            wind_speed = loaded_data['Wind_speed']
            humidity = loaded_data['Humidity']
            temperature = loaded_data['Temperature']

    # Predict the PV_production
    if st.button("Predict"):
        prediction = predict_pv_production(dhi, dni, ghi, wind_speed, humidity, temperature)
        st.success(f"Predicted PV Production: {prediction:.2f} MW")

if __name__ == "__main__":
    main()