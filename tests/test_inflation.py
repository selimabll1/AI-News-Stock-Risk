
import pandas as pd
import pytest

from ai_risk_replication.acquisition.inflation import (
    prepare_inflation_monthly,
)


def test_inflation_complete_sample(tmp_path):
    dates = pd.date_range(
        "2011-01-01", "2024-12-01", freq="MS"
    )

    # Synthetic CPI with exactly 2% annual inflation
    cpi = [
        100 * (1.02 ** (i / 12))
        for i in range(len(dates))
    ]

    path = tmp_path / "CPIAUCNS.csv"

    pd.DataFrame({
        "observation_date": dates,
        "CPIAUCNS": cpi,
    }).to_csv(path, index=False)

    result = prepare_inflation_monthly(path)

    assert len(result) == 156
    assert result["INFLATION"].isna().sum() == 0
    assert result["INFLATION"].mean() == pytest.approx(2.0)


def test_inflation_missing_month(tmp_path):
    dates = pd.date_range(
        "2011-01-01", "2024-12-01", freq="MS"
    )

    # Remove one observation from the required period
    dates = dates.delete(12)

    path = tmp_path / "CPIAUCNS.csv"

    pd.DataFrame({
        "observation_date": dates,
        "CPIAUCNS": [100.0] * len(dates),
    }).to_csv(path, index=False)

    with pytest.raises(ValueError):
        prepare_inflation_monthly(path)
