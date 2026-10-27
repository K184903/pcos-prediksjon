
from pathlib import Path
import pandas as pd
import numpy as np

# 1. Finn prosjektets rotmappe
BASE_DIR = Path(__file__).resolve().parent.parent

# 2. Finn Excel-filen
excel_path = BASE_DIR / "data/PCOS_data_without_infertility.xlsx"

# 3. Definer selvrapporterte features
selvrapport = [
    "Age (yrs)",
    "BMI",
    "Cycle(R/I)",
    "Cycle length(days)",
    "Weight gain(Y/N)",
    "hair growth(Y/N)",
    "Skin darkening (Y/N)",
    "Hair loss(Y/N)",
    "Pimples(Y/N)",
    "Reg.Exercise(Y/N)"
]

# 4. Målvariabelen
target = "PCOS (Y/N)"

# 5. Finn riktig ark i Excel-filen
excel_file = pd.ExcelFile(excel_path)
print("Ark i Excel-filen:", excel_file.sheet_names)

df = None

for sheet in excel_file.sheet_names:
    kandidat = pd.read_excel(excel_file, sheet_name=sheet)
    kandidat.columns = kandidat.columns.astype(str).str.strip()

    if all(col in kandidat.columns for col in selvrapport + [target]):
        df = kandidat
        print("Bruker ark:", sheet)
        break

if df is None:
    raise ValueError(
        "Fant ikke et Excel-ark med alle de nødvendige kolonnene. "
        "Kontroller arknavn og kolonneoverskrifter."
    )

# 6. Behold bare selvrapporterte features og målvariabelen
df_clean = df[selvrapport + [target]].copy()
df_clean["Cycle(R/I)"] = df_clean["Cycle(R/I)"].replace(5, np.nan)

# 7. Undersøk manglende verdier
print("\nManglende verdier:")
print(df_clean.isnull().sum())

# 8. Lagre datasettet som CSV
output_path = BASE_DIR / "data/pcos_cleaned.csv"
df_clean.to_csv(output_path, index=False)

print("\nDatasettet er lagret:", output_path)
print("Antall rader og kolonner:", df_clean.shape)
print("Features:", selvrapport)
