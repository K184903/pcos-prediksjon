import joblib
from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent

model = joblib.load(BASE_DIR / "pcos_model.pkl")

print(model.feature_names_in_)

person = pd.DataFrame([{
    "Age (yrs)": 25,
    "BMI": 27,
    "Cycle(R/I)": 4,
    "Cycle length(days)": 5,
    "Weight gain(Y/N)": 1,
    "hair growth(Y/N)": 1,
    "Skin darkening (Y/N)": 0,
    "Hair loss(Y/N)": 0,
    "Pimples(Y/N)": 1,
    "Reg.Exercise(Y/N)": 0
}])

sannsynlighet = model.predict_proba(person)[0, 1]
prediksjon = int(sannsynlighet >= 0.3)

print(f"Beregnet sannsynlighet for PCOS: {sannsynlighet:.1%}")
print(f"Prediksjon: {prediksjon}")