
from pathlib import Path

import pandas as pd


def prepare_treasury_monthly(path: Path) -> pd.DataFrame:
    """Prepare monthly 1-year US Treasury bill rates."""

    df = pd.read_csv(path, na_values=["."])

    df["DATE"] = pd.to_datetime(
        df["observation_date"]
    )

    df["TB1YR"] = pd.to_numeric(
        df["TB1YR"], errors="coerce"
    )

    df = df.loc[
        df["DATE"].between("2012-01-01", "2024-12-31"),
        ["DATE", "TB1YR"]
    ].sort_values("DATE").reset_index(drop=True)

    expected_dates = pd.date_range(
        "2012-01-01", "2024-12-01", freq="MS"
    )

    if df["DATE"].tolist() != expected_dates.tolist():
        raise ValueError("Incomplete monthly Treasury series.")

    if df["TB1YR"].isna().any():
        raise ValueError("Missing Treasury bill observations.")

    return df
