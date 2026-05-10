import pandas as pd
from sklearn.linear_model import LogisticRegression
import joblib
import os

# Simple dataset
data = {
    "age": [22, 25, 47, 52, 46, 56],
    "salary": [15000, 29000, 48000, 60000, 52000, 61000],
    "purchased": [0, 0, 1, 1, 1, 1]
}

df = pd.DataFrame(data)

X = df[["age", "salary"]]
y = df["purchased"]

model = LogisticRegression()
model.fit(X, y)

os.makedirs("model", exist_ok=True)
joblib.dump(model, "model/model.pkl")

print("Model trained and saved.")