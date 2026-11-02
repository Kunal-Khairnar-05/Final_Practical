import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

df = pd.read_csv("sales_data_sample.csv", encoding="latin1")
X = df[["QUANTITYORDERED", "PRICEEACH", "SALES"]]
X = StandardScaler().fit_transform(X)

# Elbow method
wcss = []
for k in range(1, 11):
    km = KMeans(n_clusters=k, n_init=10, random_state=42)
    km.fit(X)
    wcss.append(km.inertia_)

plt.plot(range(1, 11), wcss, marker="o")
plt.xlabel("Number of clusters (K)")
plt.ylabel("WCSS")
plt.title("Elbow Method")
plt.show()

# Final model with K from the elbow (bend of the curve ≈ 3)
km = KMeans(n_clusters=3, n_init=10, random_state=42)
df["Cluster"] = km.fit_predict(X)
print(df["Cluster"].value_counts())
