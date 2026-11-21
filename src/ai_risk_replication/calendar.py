"""Calendar helpers for the monthly original sample; no financial data are implied."""
from datetime import date

START_MONTH = "2012-01"
END_MONTH = "2024-12"


def parse_month(month: str) -> tuple[int, int]:
    """Parse YYYY-MM strictly, raising ValueError for invalid month strings."""
    if len(month) != 7 or month[4] != "-":
        raise ValueError(f"Expected YYYY-MM, got {month!r}")
    year, mon = month.split("-")
    if not (year.isdigit() and mon.isdigit() and len(year) == 4 and len(mon) == 2):
        raise ValueError(f"Expected YYYY-MM, got {month!r}")
    y, m = int(year), int(mon)
    date(y, m, 1)  # validates calendar month
    return y, m


def month_range(start: str = START_MONTH, end: str = END_MONTH) -> list[str]:
    """Inclusive monthly labels from start through end, e.g. 2012-01..2024-12."""
    sy, sm = parse_month(start)
    ey, em = parse_month(end)
    if (sy, sm) > (ey, em):
        raise ValueError("start month must not be later than end month")
    labels = []
    year, month = sy, sm
    while (year, month) <= (ey, em):
        labels.append(f"{year:04d}-{month:02d}")
        year, month = (year + 1, 1) if month == 12 else (year, month + 1)
    return labels
