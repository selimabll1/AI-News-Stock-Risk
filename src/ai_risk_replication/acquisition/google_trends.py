
import csv
from pathlib import Path

import pandas as pd


START = "2012-01-01"
END = "2024-12-01"
EXPECTED_MONTHS = 156


def load_trends_export(
    path: Path,
    variable_name: str,
) -> pd.DataFrame:
    """
    Import an original Google Trends CSV export.

    The export must contain monthly observations
    from January 2012 through December 2024.

    Original source:
    Salisu & Badmus (2026), Google Trends.
    """
    path = Path(path)

    if not path.exists():
        raise FileNotFoundError(
            f"Google Trends file not found: {path}"
        )

    # The original CSV may contain metadata lines
    # before the actual Month header.
    with path.open(
        "r", encoding="utf-8-sig", newline=""
    ) as file:
        rows = list(csv.reader(file))

    
# Accept monthly Google Trends exports in
# English, French, Spanish, or German.
    MONTH_HEADERS = {
        "month",
        "mois",
        "mes",
        "monat",
    }

    header_index = next(
    (
        i for i, row in enumerate(rows)
        if row
        and row[0].strip().casefold() in MONTH_HEADERS
    ),
    None,
)


    if header_index is None:
        raise ValueError(
            "Monthly Google Trends header not found. "
            "Check that you exported Interest over time."
        )

    observations = []

    for row in rows[header_index + 1:]:
        if len(row) < 2 or not row[0].strip():
            continue

        date_text = row[0].strip()
        value_text = row[1].strip()

        if value_text == "<1":
            raise ValueError(
                f"Google Trends returned '<1' for "
                f"{date_text}. This requires a documented "
                "treatment before estimation."
            )

        observations.append(
            (date_text, value_text)
        )

    if not observations:
        raise ValueError(
            "No observations found in the CSV."
        )

    df = pd.DataFrame(
        observations,
        columns=["DATE", variable_name],
    )

    df["DATE"] = pd.to_datetime(
        df["DATE"], errors="raise"
    ).dt.to_period("M").dt.to_timestamp()

    df[variable_name] = pd.to_numeric(
        df[variable_name], errors="raise"
    )

    if df["DATE"].duplicated().any():
        raise ValueError("Duplicate monthly dates detected.")

    df = df.sort_values("DATE").reset_index(drop=True)

    expected_dates = pd.date_range(
        START, END, freq="MS"
    )

    if df["DATE"].tolist() != expected_dates.tolist():
        raise ValueError(
            "The export must contain exactly the "
            "156 months from January 2012 "
            "through December 2024."
        )

    if (
        df[variable_name].isna().any()
        or not df[variable_name].between(0, 100).all()
    ):
        raise ValueError(
            "Google Trends values must be "
            "numeric and between 0 and 100."
        )

    return df
