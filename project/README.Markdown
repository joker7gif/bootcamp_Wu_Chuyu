### Data source: After trying the Polygon.io Demo API and the Finnhub Demo API, I ultimately chose yfinance because it’s the simplest way to obtain real, real-time data, and I want my project to be as practical as possible.

## Stage1
## 1. Short Project Summary 
# What problem am I solving and why does it matter?
Tesla (TSLA) has been one of the most volatile and closely watched stocks in recent years. Investors often lack clear, data-driven insight into its performance trends and risk profile. This project analyzes Tesla’s stock price movements over the past three years using real market data from Yahoo Finance. By examining return patterns, volatility, and market reactions, we aim to provide a structured foundation for evaluating whether TSLA aligns with specific investment strategies.
This matters because retail investors, small portfolio managers, and analysts need quick yet rigorous insights. Instead of relying solely on media coverage or speculation, this project leverages historical price data to reveal actionable signals and a clearer understanding of Tesla’s market behavior

## 2. Stakeholder Persona / Context Description
# Who will use my results
Primary Stakeholders: Retail investors, individual traders, and small-scale asset managers.
Secondary Stakeholders: Finance students or researchers interested in practical stock analysis workflows.
# What do they care about
Clear performance metrics: Historical returns, risk levels, and market behavior.
Time efficiency: Easy-to-read visualizations and metrics instead of raw tables or lengthy reports.
Practicality: Real, up-to-date market data rather than synthetic or outdated examples.

## Stage2
# Easy,same as homework

## Stage3
# Python Fundamentals
This stage demonstrates basic **Python, NumPy, and pandas** operations with toy data.
Includes `notebooks/python_fundamentals_summary.ipynb` and `src/utils.py` with a reusable function.
Optional: extra utilities, documentation, or basic tests.
All files are organized for use in later **EDA and modeling stages**.
Committed and pushed to GitHub for project continuity.

## Stage4
# Tesla Stock Data Ingestion
## Overview
This project demonstrates data acquisition and ingestion using `yfinance`.
We fetch Tesla (TSLA) stock history for the past 3 years and save it to `/data/TSLA/`.
## How to Run
1. Copy `.env.example` to `.env`
2. Adjust any paths or API keys if needed
3. Run:
   ```bash
   python src/fetch_data.py

## Stage 5: Data Storage
In this stage, reusable functions for saving and loading data were implemented in src/data_io.py.
Raw data is stored as CSV in /data/raw/ for easy inspection.
Processed data is stored as Parquet in /data/processed/ for efficiency.
A sample notebook demonstrates downloading data, saving it using these functions, and reloading it for later stages.

## Stage 6: Data Preprocessing
In this stage, raw Tesla stock data was cleaned and prepared for modeling.
Steps included removing invalid rows, converting columns to numeric types, handling missing values, removing outliers, and normalizing key features.
Reusable preprocessing functions were stored in src1/cleaning.py.
The cleaned dataset was saved to /data/processed/TSLA_cleaned.csv for downstream modeling.

## Stage 7 Outlier Analysis
This stage implements explicit outlier detection and removal using the IQR method.
All reusable functions are stored in src1/outliers.py and integrated into the pipeline.
Data is reloaded from Stage 6 outputs, cleaned for extreme values, and saved again.
Outlier handling assumptions and potential impacts are documented for future modeling.