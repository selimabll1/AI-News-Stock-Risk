
from pytrends.request import TrendReq

pytrends = TrendReq(hl="en-US", tz=0)

for name, search_type in [
    ("web", ""),
    ("news", "news"),
]:
    pytrends.build_payload(
        kw_list=["Artificial Intelligence"],
        cat=0,
        timeframe="2012-01-01 2024-12-31",
        geo="",
        gprop=search_type,
    )

    df = pytrends.interest_over_time()

    if df.empty:
        print(name, "No observations returned")
        continue

    values = df["Artificial Intelligence"]

    print(f"\n{name.upper()}")
    print("Observations:", len(values))
    print("Mean:", round(values.mean(), 3))
    print("Std:", round(values.std(), 3))
    print("Maximum:", values.max())

    print("First months:")
    print(values.head())

    print("Peak month:", values.idxmax())

    df.to_csv(
        f"data/raw/google_trends/pytrends_{name}.csv"
    )
