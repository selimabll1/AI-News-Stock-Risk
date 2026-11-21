
from pathlib import Path
from urllib.request import urlretrieve

import pandas as pd


# ============================================================
# Configuration — Salisu & Badmus (2026)
# ============================================================

VIX_URL = (
    "https://fred.stlouisfed.org/graph/fredgraph.csv"
    "?id=VIXCLS"
)

START_DATE = "2012-01-01"
END_DATE = "2024-12-31"

EXPECTED_MONTHS = 156


# ============================================================
# VIX Acquisition and Processing
# ============================================================

def download_vix(
    raw_path: Path,
    processed_path: Path,
) -> pd.DataFrame:
    """
    Download the CBOE Volatility Index (VIXCLS) from FRED.

    Reproduce the monthly aggregation described in:
    Salisu, A. A., & Badmus, S. (2026).
    Can AI News Improve the Out-of-Sample Forecasts of
    Risk Premia and Volatility in the U.S. Stock Market?

    Methodology:
        1. Download the original daily VIXCLS series.
        2. Preserve the raw CSV.
        3. Restrict observations to January 2012 -
           December 2024.
        4. Convert daily observations into monthly
           arithmetic averages.
        5. Validate the resulting monthly series.
        6. Save the processed dataset.
    """

    raw_path = Path(raw_path)
    processed_path = Path(processed_path)

    # --------------------------------------------------------
    # Step 1: Create directories
    # --------------------------------------------------------

    raw_path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    processed_path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    # --------------------------------------------------------
    # Step 2: Download original FRED data
    # --------------------------------------------------------

    print("Downloading VIXCLS from FRED...")

    urlretrieve(
        VIX_URL,
        raw_path,
    )

    # --------------------------------------------------------
    # Step 3: Load the original dataset
    # --------------------------------------------------------

    df = pd.read_csv(raw_path)

    # Normalize column names for compatibility with
    # different FRED CSV formats.
    df.columns = (
        df.columns
        .str.strip()
        .str.upper()
    )

    # FRED may use "observation_date" or "DATE".
    # Convert both formats to one consistent name.
    df = df.rename(
        columns={
            "OBSERVATION_DATE": "DATE",
        }
    )

    required_columns = {"DATE", "VIXCLS"}

    if not required_columns.issubset(df.columns):
        raise ValueError(
            "Unexpected FRED CSV format. "
            f"Available columns: {df.columns.tolist()}"
        )

    print("Original dataset loaded successfully.")
    print("Original observations:", len(df))

    # --------------------------------------------------------
    # Step 4: Convert data types
    # --------------------------------------------------------

    df["DATE"] = pd.to_datetime(
        df["DATE"],
        errors="raise",
    )

    df["VIXCLS"] = pd.to_numeric(
        df["VIXCLS"],
        errors="coerce",
    )

    # --------------------------------------------------------
    # Step 5: Filter original research period
    # --------------------------------------------------------

    df = df.loc[
        (df["DATE"] >= START_DATE)
        & (df["DATE"] <= END_DATE)
    ].copy()

    if df.empty:
        raise ValueError(
            "No VIX observations found for "
            "the research period."
        )

    if df["DATE"].duplicated().any():
        raise ValueError(
            "Duplicate daily dates detected."
        )

    df = df.sort_values("DATE")

    print(
        "Filtered daily observations:",
        len(df),
    )

    # --------------------------------------------------------
    # Step 6: Daily to monthly aggregation
    # --------------------------------------------------------

    # The original article aggregates daily VIXCLS
    # observations using monthly arithmetic averages.
    # Missing daily values are excluded from the mean.

    monthly = (
        df.set_index("DATE")["VIXCLS"]
        .resample("MS")
        .mean()
        .rename("VIX")
        .reset_index()
    )

    # --------------------------------------------------------
    # Step 7: Validate results
    # --------------------------------------------------------

    if len(monthly) != EXPECTED_MONTHS:
        raise ValueError(
            f"Expected {EXPECTED_MONTHS} months, "
            f"but found {len(monthly)}."
        )

    if monthly["VIX"].isna().any():
        missing_months = monthly.loc[
            monthly["VIX"].isna(),
            "DATE",
        ]

        raise ValueError(
            "Missing monthly VIX observations: "
            f"{missing_months.tolist()}"
        )

    if (
        monthly["DATE"].iloc[0]
        != pd.Timestamp("2012-01-01")
    ):
        raise ValueError(
            "Unexpected first monthly observation."
        )

    if (
        monthly["DATE"].iloc[-1]
        != pd.Timestamp("2024-12-01")
    ):
        raise ValueError(
            "Unexpected last monthly observation."
        )

    # --------------------------------------------------------
    # Step 8: Save processed dataset
    # --------------------------------------------------------

    monthly.to_csv(
        processed_path,
        index=False,
    )

    # --------------------------------------------------------
    # Step 9: Display summary
    # --------------------------------------------------------

    print("\nVIX acquisition completed successfully.")
    print("-----------------------------------")
    print("Source: FRED - VIXCLS")
    print("Period: 2012-01 to 2024-12")
    print("Frequency: Monthly")
    print("Aggregation: Daily arithmetic mean")
    print("Monthly observations:", len(monthly))
    print("Missing values:", monthly["VIX"].isna().sum())
    print("Mean VIX:", round(monthly["VIX"].mean(), 4))
    print("Minimum VIX:", round(monthly["VIX"].min(), 4))
    print("Maximum VIX:", round(monthly["VIX"].max(), 4))
    print("Raw file:", raw_path)
    print("Processed file:", processed_path)

    return monthly
