
from pathlib import Path

from ai_risk_replication.acquisition.fred import (
    download_vix,
)


PROJECT_ROOT = Path(__file__).resolve().parents[1]

raw = PROJECT_ROOT / "data/raw/fred/VIXCLS.csv"

processed = (
    PROJECT_ROOT
    / "data/processed/vix_monthly.csv"
)

monthly = download_vix(raw, processed)

print("VIX acquisition successful.")
print("Observations:", len(monthly))
print(monthly.head())
print(monthly.tail())
