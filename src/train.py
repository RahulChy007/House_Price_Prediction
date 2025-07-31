# train.py
import pandas as pd
import os
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import joblib

# 1. Load dataset
# data_path = os.path.join("..", "data", "raw", "housing.csv")
df = pd.read_csv("../data/raw/housing.csv")

# 2. Features and target
X = df.drop("price", axis=1)
y = df["price"]

# 3. Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# 5. Evaluate the model
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Model trained.")
print(f"Mean Squared Error: {mse:.2f}")
print(f"R² Score: {r2:.2f}")

# 6. Save the model
model_dir = os.path.join("..", "models")
os.makedirs(model_dir, exist_ok=True)
model_path = os.path.join(model_dir, "model.pkl")
joblib.dump(model, model_path)

print(f"Model saved to {model_path}")
