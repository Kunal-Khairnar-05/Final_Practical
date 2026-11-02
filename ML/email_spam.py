import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

df = pd.read_csv("emails.csv")
X = df.drop(columns=["Email No.", "Prediction"])     # word-count columns
y = df["Prediction"]                                 # 1 = spam, 0 = not spam

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

for name, model in [("KNN", KNeighborsClassifier(n_neighbors=5)),
                    ("SVM", SVC(kernel="linear"))]:
    model.fit(X_train, y_train)
    pred = model.predict(X_test)
    print("=====", name, "=====")
    print("Accuracy:", accuracy_score(y_test, pred))
    print(confusion_matrix(y_test, pred))
    print(classification_report(y_test, pred))
