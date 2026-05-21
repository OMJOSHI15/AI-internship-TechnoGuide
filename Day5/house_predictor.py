import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv("house_data.csv")

# Input and output
X = data[["Area"]]
y = data["Price"]

# Create model
model = LinearRegression()

# Train model
model.fit(X, y)

# Predict house price
prediction = model.predict([[1000]])

print("Predicted House Price:", prediction[0])

# Graph
plt.scatter(X, y)

plt.plot(X, model.predict(X))

plt.xlabel("Area")
plt.ylabel("Price")
plt.title("House Price Prediction")

plt.show()