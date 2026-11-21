"""Minimal environment verification; run after `pip install -e .`."""
from ai_risk_replication import __version__
from ai_risk_replication.calendar import month_range


def main() -> None:
    months = month_range()
    print(f"ai-risk-replication v{__version__}")
    print(f"Reference sample: {months[0]} -> {months[-1]} ({len(months)} months)")
    print("No financial data have been downloaded or estimated.")


if __name__ == "__main__":
    main()
