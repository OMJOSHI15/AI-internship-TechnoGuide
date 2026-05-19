import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

# Dataset
data = pd.DataFrame({
    "Area": [500, 700, 900, 1100, 1300],
    "Price": [100000, 150000, 200000, 250000, 300000]
})

# Inputs and outputs
X = data[["Area"]]
y = data["Price"]

# Train model
model = LinearRegression()
model.fit(X, y)

# Website title
st.title("🏠 House Price Predictor")

# User input
area = st.number_input("Enter house area")

# Prediction
if st.button("Predict Price"):
    prediction = model.predict([[area]])

    st.success(f"Predicted Price: ₹{prediction[0]:,.2f}")
