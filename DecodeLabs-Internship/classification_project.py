import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score

iris_data = load_iris()
X = iris_data.data
y = iris_data.target


iris_df = pd.DataFrame(X, columns=iris_data.feature_names)
iris_df['target'] = y
print("--- Check Data ---")
print(iris_df.head(), "\n")


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)

data_scaler = StandardScaler()
X_train_scaled = data_scaler.fit_transform(X_train)
X_test_scaled = data_scaler.transform(X_test)


knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train_scaled, y_train)

y_pred = knn.predict(X_test_scaled)


model_acc = accuracy_score(y_test, y_pred)
matrix = confusion_matrix(y_test, y_pred)

print("=== Final Results ===")
print(f"Accuracy Score: {model_acc * 100:.2f}%")
print("\nConfusion Matrix:")
print(matrix)

print("\nClassification Report:")
print(classification_report(y_test, y_pred, target_names=iris_data.target_names))