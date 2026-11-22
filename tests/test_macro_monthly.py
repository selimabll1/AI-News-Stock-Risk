
from pathlib import Path

import pandas as pd
import pytest


ROOT = Path(__file__).resolve().parents[1]
PROCESSED = ROOT / "data/processed"


def test_macro_matches_processed_sources():

    files = [
        "ai_trends_monthly.csv",
        "vix_monthly.csv",
        "treasury_monthly.csv",
        "inflation_monthly.csv",
        "macro_monthly.csv",
    ]

    # Data files are excluded from Git.
    # Skip the integration check if they are unavailable.
    if not all((PROCESSED / f).exists() for f in files):
        pytest.skip("Local processed datasets unavailable")

    def load(filename):
        return pd.read_csv(
            PROCESSED / filename,
            parse_dates=["DATE"],
        )

    expected = load("ai_trends_monthly.csv")

    for filename in files[1:-1]:
        expected = expected.merge(
            load(filename),
            on="DATE",
            validate="one_to_one",
        )

    actual = load("macro_monthly.csv")

    pd.testing.assert_frame_equal(
        actual,
        expected[actual.columns],
        check_exact=False,
        rtol=1e-12,
    )

    assert len(actual) == 156
    assert actual["DATE"].is_unique
    assert not actual.isna().any().any()
    assert actual["DATE"].iloc[0] == pd.Timestamp("2012-01-01")
    assert actual["DATE"].iloc[-1] == pd.Timestamp("2024-12-01")
