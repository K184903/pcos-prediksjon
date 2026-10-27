from pathlib import Path

import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix
import joblib

#Finner datasettet
BASE_DIR = Path(__file__).resolve().parent.parent
data_path = BASE_DIR / "data/pcos_cleaned.csv"

df = pd.read_csv(data_path)

#Features og målvariabel
X = df.drop(columns=["PCOS (Y/N)"])
y = df["PCOS (Y/N)"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)
X_train, X_val, y_train, y_val = train_test_split(
    X_train,
    y_train,
    test_size=0.25,
    random_state=42,
    stratify=y_train
)

print("Treningsdata:", X_train.shape)
print("Testdata:", X_test.shape)

model = Pipeline([
    ("imputer", SimpleImputer(strategy="most_frequent")),
    ("scaler", StandardScaler()),
    ("classifier", LogisticRegression(max_iter=1000))
])

model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print("Prediksjoner:", y_pred)
print("Faktiske verdier:", y_test.values)

print(classification_report(y_test, y_pred))
print(confusion_matrix(y_test, y_pred))

y_proba = model.predict_proba(X_test)[:, 1]

print("Sannsynlighet for PCOS:")
print(y_proba[:10])

val_proba = model.predict_proba(X_val)[:, 1]
val_pred_03 = (val_proba >= 0.3).astype(int)


print(classification_report(y_val, val_pred_03))

val_pred_05 = (val_proba>= 0.5).astype(int)
print(classification_report(y_val, val_pred_05))

test_proba = model.predict_proba(X_test)[:, 1]
test_pred = (test_proba >= 0.3).astype(int)

print("Enedelig evaluering av testsettet:")
print(classification_report(y_test, test_pred))
print(confusion_matrix(y_test, test_pred))

joblib.dump(model, BASE_DIR / "pcos_model.pkl")


