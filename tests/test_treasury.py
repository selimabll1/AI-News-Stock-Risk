
import pandas as pd
import pytest

from ai_risk_replication.acquisition.treasury import (
    prepare_treasury_monthly,
)


def test_treasury_complete_sample(tmp_path):
    dates = pd.date_range(
        "2012-01-01", "2024-12-01", freq="MS"
    )

    path = tmp_path / "TB1YR.csv"

    pd.DataFrame({
        "observation_date": dates,
        "TB1YR": [1.5] * len(dates),
    }).to_csv(path, index=False)

    result = prepare_treasury_monthly(path)

    assert len(result) == 156
    assert result["TB1YR"].isna().sum() == 0
    assert result["TB1YR"].mean() == pytest.approx(1.5)


def test_treasury_missing_month(tmp_path):
    dates = pd.date_range(
        "2012-01-01", "2024-12-01", freq="MS"
    )

    path = tmp_path / "TB1YR.csv"

    pd.DataFrame({
        "observation_date": dates[:-1],
        "TB1YR": [1.5] * (len(dates) - 1),
    }).to_csv(path, index=False)

    with pytest.raises(ValueError):
        prepare_treasury_monthly(path)
