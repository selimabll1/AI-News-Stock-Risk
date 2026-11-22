
from pathlib import Path

from ai_risk_replication.acquisition.inflation import (
    prepare_inflation_monthly,
)

ROOT = Path(__file__).resolve().parents[1]

RAW = ROOT / "data/raw/fred/CPIAUCNS.csv"
OUTPUT = ROOT / "data/processed/inflation_monthly.csv"

df = prepare_inflation_monthly(RAW)

OUTPUT.parent.mkdir(parents=True, exist_ok=True)
df.to_csv(OUTPUT, index=False)

print("\nUS inflation preparation completed.")
print("-----------------------------------")
print("Source: FRED - CPIAUCNS")
print("Method: Year-over-year CPI percentage change")
print("Period: 2012-01 to 2024-12")
print("Observations:", len(df))
print("Missing:", df["INFLATION"].isna().sum())
print("Mean:", round(df["INFLATION"].mean(), 6))
print("Std:", round(df["INFLATION"].std(), 6))
print("\nSaved to:", OUTPUT)
