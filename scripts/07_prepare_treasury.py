
from pathlib import Path

from ai_risk_replication.acquisition.treasury import (
    prepare_treasury_monthly,
)

ROOT = Path(__file__).resolve().parents[1]

RAW = ROOT / "data/raw/fred/TB1YR.csv"
OUTPUT = ROOT / "data/processed/treasury_monthly.csv"

# Load and validate the monthly Treasury series
df = prepare_treasury_monthly(RAW)

# Save the processed observations
OUTPUT.parent.mkdir(parents=True, exist_ok=True)
df.to_csv(OUTPUT, index=False)

print("\nTreasury acquisition completed.")
print("--------------------------------")
print("Source: FRED - TB1YR")
print("Period: 2012-01 to 2024-12")
print("Frequency: Monthly")
print("Observations:", len(df))
print("Missing values:", df["TB1YR"].isna().sum())
print("Mean rate:", round(df["TB1YR"].mean(), 6))
print("\nFirst observations:")
print(df.head())
print("\nLast observations:")
print(df.tail())
print("\nSaved to:", OUTPUT)
