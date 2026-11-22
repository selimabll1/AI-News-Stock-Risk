
from pathlib import Path

from ai_risk_replication.acquisition.google_trends import (
    load_trends_export,
)


ROOT = Path(__file__).resolve().parents[1]

RAW = ROOT / "data/raw/google_trends"
PROCESSED = ROOT / "data/processed"

PROCESSED.mkdir(parents=True, exist_ok=True)

# Import the two original Google Trends exports.
news = load_trends_export(
    RAW / "ai_news_search.csv",
    "AI_NEWS",
)

web = load_trends_export(
    RAW / "ai_web_search.csv",
    "AI_WEB",
)

# Align on the monthly date.
merged = news.merge(
    web,
    on="DATE",
    how="inner",
    validate="one_to_one",
)

if len(merged) != 156:
    raise ValueError("Unexpected merged sample size.")

# Save the research-ready dataset.
output = PROCESSED / "ai_trends_monthly.csv"
merged.to_csv(output, index=False)

print("\nGoogle Trends acquisition completed.")
print("Monthly observations:", len(merged))
print("Missing values:")
print(merged.isna().sum())
print("\nDescriptive statistics:")
print(merged[["AI_NEWS", "AI_WEB"]].describe())
print("\nFirst observations:")
print(merged.head())
print("\nLast observations:")
print(merged.tail())
print("\nSaved to:", output)
