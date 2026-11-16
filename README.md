# AI News and Stock Market Risk Forecasting

## Research Project

This project investigates whether artificial intelligence-related news and Google search interest can improve the out-of-sample forecasting of stock market risk premia and volatility in the United States.

**Study period:** 2012–2024

**Reference paper:** Salisu & Badmus (2026), *Can AI News Improve the Out-of-Sample Forecasts of Risk Premia and Volatility in the U.S. Stock Market?*

**DOI:** [10.1007/s11135-026-02816-9](https://doi.org/10.1007/s11135-026-02816-9)

## Objectives

- Reproduce the main empirical methodology of the reference paper.
- Construct AI-related news and search interest indicators.
- Compare AI-related stocks with conventional stocks.
- Estimate econometric models for risk premia and volatility.
- Evaluate out-of-sample forecasting performance.
- Conduct robustness checks and interpret the results.

## Project Structure

```text
math_finance_project/
├── notebooks/
├── data/
│   ├── raw/
│   └── clean/
├── outputs/
│   ├── figures/
│   ├── tables/
│   └── models/
├── docs/
├── report/
├── .gitignore
├── README.md
└── requirements.txt
```

## Technology

- Python 3.11
- Jupyter Notebook
- Pandas and NumPy
- SciPy and Statsmodels
- Scikit-learn
- Matplotlib and Seaborn
- yfinance and pytrends

## Reproducibility

Project dependencies are listed in `requirements.txt`.

## Research Transparency

The project will distinguish between:

- Direct replications of the reference paper.
- Data-source substitutions and methodological adaptations.
- Additional robustness checks and research extensions.