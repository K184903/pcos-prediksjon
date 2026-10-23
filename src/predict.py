import joblib
import pandas as pd
from pathlib import Path

MODEL_PATH = Path(__file__).resolve().parent.parent / "model" / "pcos_model.joblib"
_lagret = joblib.load(MODEL_PATH)

MODELL = _lagret["model"]
FEATURES = _lagret["features"]
GRONN, ROD = _lagret["terskler"]


def _ja_nei(svar):
    if svar == "Ja":
        return 1.0
    if svar == "Nei":
        return 0.0
    return 0.5  # "usikker"


def prediker(svar: dict) -> str:
    rad = {
        "Age (yrs)": svar["alder"],
        "BMI": svar["bmi"],
        "Irregular cycle": _ja_nei(svar["syklus"]),
        "Bleeding days": svar["blodningsdager"],
        "Weight gain(Y/N)": _ja_nei(svar["vektokning"]),
        "hair growth(Y/N)": _ja_nei(svar["hoervekst"]),
        "Skin darkening (Y/N)": _ja_nei(svar["hudpartier"]),
        "Hair loss(Y/N)": _ja_nei(svar["hoertap"]),
        "Pimples(Y/N)": _ja_nei(svar["akne"]),
        "Reg.Exercise(Y/N)": _ja_nei(svar["trening"]),
    }
    df = pd.DataFrame([rad])[FEATURES]  # sikrer riktig kolonnerekkefølge
    p = MODELL.predict_proba(df)[0, 1]

    if p < GRONN:
        return "grønt"
    if p >= ROD:
        return "rødt"
    return "gult"

