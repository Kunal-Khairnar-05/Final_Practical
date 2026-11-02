import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_squared_error

df = pd.read_csv("uber.csv")

# 1. Pre-process
df = df.drop(columns=["Unnamed: 0", "key"])
df = df.dropna()
df["pickup_datetime"] = pd.to_datetime(df["pickup_datetime"])
df["hour"] = df["pickup_datetime"].dt.hour
df = df.drop(columns=["pickup_datetime"])
df["distance"] = np.sqrt((df["dropoff_longitude"] - df["pickup_longitude"])**2 +
                         (df["dropoff_latitude"] - df["pickup_latitude"])**2) * 111   # approx km

# 2. Outliers (boxplot + IQR removal)
df.boxplot(column=["fare_amount", "distance"])
plt.show()
for col in ["fare_amount", "distance"]:
    q1, q3 = df[col].quantile(0.25), df[col].quantile(0.75)
    iqr = q3 - q1
    df = df[(df[col] >= q1 - 1.5 * iqr) & (df[col] <= q3 + 1.5 * iqr)]

# 3. Correlation
print(df.corr())

# 4. Models
X = df.drop("fare_amount", axis=1)
y = df["fare_amount"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 5. Evaluate & compare
for name, model in [("Linear Regression", LinearRegression()),
                    ("Random Forest", RandomForestRegressor(n_estimators=50, n_jobs=-1))]:
    model.fit(X_train, y_train)
    pred = model.predict(X_test)
    print(name, "-> R2:", r2_score(y_test, pred),
          " RMSE:", np.sqrt(mean_squared_error(y_test, pred)))
