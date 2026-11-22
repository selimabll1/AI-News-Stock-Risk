
from pathlib import Path

import pandas as pd


def prepare_inflation_monthly(path: Path) -> pd.DataFrame:
    """Compute US year-over-year CPI inflation (percent)."""

    df = pd.read_csv(path, na_values=["."])

    df["DATE"] = pd.to_datetime(
        df["observation_date"]
    )

    df["CPI"] = pd.to_numeric(
        df["CPIAUCNS"], errors="coerce"
    )

    df = (
        df[["DATE", "CPI"]]
        .sort_values("DATE")
        .reset_index(drop=True)
    )

    if df["DATE"].duplicated().any():
        raise ValueError("Duplicate CPI dates detected.")

    # Verify the complete input window, including 2011.
    required_dates = pd.date_range(
        "2011-01-01", "2024-12-01", freq="MS"
    )

    source = df.set_index("DATE").reindex(required_dates)

    if source["CPI"].isna().any():
        raise ValueError("Missing CPI observations.")

    if (source["CPI"] <= 0).any():
        raise ValueError("CPI must be strictly positive.")

    # Year-over-year percentage change
    source["INFLATION"] = (
        100 * (source["CPI"] / source["CPI"].shift(12) - 1)
    )

    result = (
        source.loc["2012-01-01":"2024-12-01", ["INFLATION"]]
        .rename_axis("DATE")
        .reset_index()
    )

    if len(result) != 156 or result["INFLATION"].isna().any():
        raise ValueError("Incomplete inflation sample.")

    return result
