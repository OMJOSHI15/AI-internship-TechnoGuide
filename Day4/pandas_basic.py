import pandas as pd

data = pd.read_csv("student.csv")

print("Dataset:\n")
print(data)

print("\nAverage Maths Marks:")
print(data["Maths"].mean())

print("\nHighest Science Marks:")
print(data["Science"].max())