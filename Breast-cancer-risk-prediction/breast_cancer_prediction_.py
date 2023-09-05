import streamlit as st
import joblib
import numpy as np
import requests

# Define the Streamlit app title
st.title("Breast Cancer Risk Prediction")

# Load the machine learning model from GitHub
@st.cache(allow_output_mutation=True)
def load_model():
    model_url = "https://github.com/NarayananM264059/Technex/raw/main/Breast-cancer-risk-prediction/data/clf_svc_model.pkl"
    model = joblib.load(requests.get(model_url, stream=True).raw)
    return model

model = load_model()

# Create input components for user interaction
radius_mean = st.slider("Mean Radius (0-30)", 0.0, 30.0, 15.0)
texture_mean = st.slider("Mean Texture (0-30)", 0.0, 30.0, 15.0)
compactness_mean = st.slider("Mean Compactness (0-1)", 0.0, 1.0, 0.5)
perimeter_mean = st.slider("Mean Perimeter (0-200)", 0.0, 200.0, 100.0)
area_mean = st.slider("Mean Area (0-2500)", 0.0, 2500.0, 1250.0)
smoothness_mean = st.slider("Mean Smoothness (0-0.25)", 0.0, 0.25, 0.125)
concavity_mean = st.slider("Mean Concavity (0-1)", 0.0, 1.0, 0.5)
concave_points_mean = st.slider("Mean Concave Points (0-0.25)", 0.0, 0.25, 0.125)
symmetry_mean = st.slider("Mean Symmetry (0-0.5)", 0.0, 0.5, 0.25)
fractal_dimension_mean = st.slider("Mean Fractal Dimension (0-0.05)", 0.0, 0.05, 0.025)

# Create a button to trigger prediction
if st.button("Predict"):
    # Prepare the input data for prediction
    input_data = np.array([[radius_mean, texture_mean, compactness_mean, perimeter_mean, area_mean, smoothness_mean,
                            concavity_mean, concave_points_mean, symmetry_mean, fractal_dimension_mean]])

    # Make a prediction using the loaded model
    prediction = model.predict(input_data)

    # Display the prediction result
    if prediction[0] == 0:
        st.error("Prediction: Malignant (Class 0)")
    else:
        st.success("Prediction: Benign (Class 1)")
