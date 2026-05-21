import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Dataset
hours = [[1], [2], [3], [4], [5]]
marks = [20, 40, 50, 70, 90]

# Model
model = LinearRegression()

# Train model
model.fit(hours, marks)

# Prediction
predicted = model.predict([[6]])

print("Predicted marks for 6 study hours:", predicted[0])

# Graph
plt.scatter(hours, marks)

plt.plot(hours, model.predict(hours))

plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.title("Study Hours vs Marks")

plt.show()