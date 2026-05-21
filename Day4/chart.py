import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("student.csv")

plt.bar(data["Name"], data["Maths"])

plt.xlabel("Students")
plt.ylabel("Maths Marks")
plt.title("Student Maths Performance")

plt.show()