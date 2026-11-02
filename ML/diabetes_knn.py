import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score

df = pd.read_csv("diabetes.csv")
X = df.iloc[:, :-1]          # all columns except last
y = df.iloc[:, -1]           # Outcome

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)
pred = knn.predict(X_test)

acc = accuracy_score(y_test, pred)
print("Confusion Matrix:\n", confusion_matrix(y_test, pred))
print("Accuracy  :", acc)
print("Error rate:", 1 - acc)
print("Precision :", precision_score(y_test, pred))
print("Recall    :", recall_score(y_test, pred))
