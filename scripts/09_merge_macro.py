
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
PROCESSED = ROOT / "data/processed"

sources = {
    "Google Trends": "ai_trends_monthly.csv",
    "VIX": "vix_monthly.csv",
    "Treasury": "treasury_monthly.csv",
    "Inflation": "inflation_monthly.csv",
}

expected_dates = pd.date_range(
    "2012-01-01",
    "2024-12-01",
    freq="MS",
)

frames = []

for name, filename in sources.items():
    df = pd.read_csv(
        PROCESSED / filename,
        parse_dates=["DATE"],
    )

    if df["DATE"].duplicated().any():
        raise ValueError(f"Duplicate dates in {name}")

    if not pd.DatetimeIndex(df["DATE"]).equals(expected_dates):
        raise ValueError(f"Calendar mismatch in {name}")

    frames.append(df)

# Strict one-to-one merge
macro = frames[0]

for df in frames[1:]:
    macro = macro.merge(
        df,
        on="DATE",
        how="inner",
        validate="one_to_one",
    )

macro = macro[
    ["DATE", "AI_NEWS", "AI_WEB",
     "VIX", "TB1YR", "INFLATION"]
]

if len(macro) != 156:
    raise ValueError("Expected 156 monthly observations.")

if macro.isna().any().any():
    raise ValueError("Missing values detected.")

output = PROCESSED / "macro_monthly.csv"
macro.to_csv(output, index=False)

print("\nMacroeconomic dataset completed.")
print("--------------------------------")
print("Observations:", len(macro))
print("Missing values:", macro.isna().sum().sum())

print("\nDescriptive statistics:")
print(
    macro.drop(columns="DATE")
    .agg(["mean", "std", "min", "max"])
    .round(4)
)

print("\nFirst observations:")
print(macro.head())

print("\nSaved to:", output)
