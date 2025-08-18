# bootcamp_Wu_Chuyu
## Folder Structure
- **homework/** → All homework contributions will be submitted here.
- **project/** → All project contributions will be submitted here.
- **class_materials/** → Local storage for class materials. Never pushed to
GitHub.

## Homework Folder Rules
- Each homework will be in its own subfolder (`homework0`, `homework1`, etc.)
- Include all required files for grading.
## Project Folder Rules
- Keep project files organized and clearly named.




## Stage1
# Project: [ETF strategy prediction]

## Scoping Paragraph

**Problem:**  
Will this ETF strategy still work next year? This matters for ensuring ongoing performance and risk control for investors.

**Stakeholder:**  
Portfolio Manager (PM)

**User:**  
PM and Quantitative Analyst

**Useful Answer Type:**  
Predictive intervals and plain-language forward scenarios

**Decision Trigger:**  
Weekly ETF rebalance meeting

**Assumptions & Constraints:**  
- Stationarity of return drivers, market liquidity, realistic trade capacity
- Constraints: Data latency < 1 day, compliance rules

**Known Unknowns / Risks:**  
- Regime change/market shifts
- Cost drift (fees/slippage)
- Benchmark mismatch

**Lifecycle Mapping & Minimal Repo Plan**

| Goal                        | Stage                  | Deliverable(s)                      |
|-----------------------------|------------------------|-------------------------------------|
| Inform weekly ETF rebalance | Problem Framing & Scoping | Scoping paragraph, persona, repo skeleton |
| Build/validate forecast     | Modeling & Validation  | Notebooks, test results             |
| Monitor/update assumptions  | Deployment & Monitoring| Monitoring hooks, docs              |

**Repo Structure:**
- /data/        # Raw and processed data (no sensitive info pushed)
- /src/         # Reusable code modules/scripts
- /notebooks/   # EDA, numbered experiments
- /docs/        # Memos, personas, design notes
- README.md     # This file

---

## How to Use

- Start all work in notebooks and scripts here.
- Add new assumptions, risks, and learnings to README and /docs/ as you go.
- Validate all assumptions and document results.



## Stage2
# “Environment & Config Check”



## Stage3
# 1. NumPy Operations
 Create an array and perform elementwise operations.
 Compare loop vs vectorized execution.
# 2. Dataset Loading
 Load provided CSV (data/starter_data.csv) using pandas.
 Inspect with .info() and .head().
# 3. Summary Statistics
 Calculate .describe() for numeric columns.
 Perform .groupby() aggregation by category.
# 4. Save Outputs
 Save summary stats to data/processed/summary.csv or .json.
 Bonus: Create and save a basic plot.
# 5. Reusable Functions
 Write at least one utility function (get_summary_stats(df)).
 Bonus: Move function to src/utils.py and import in notebook


 ## Stage4
 # PART1 
 url = 'https://www.alphavantage.co/query'
 # PART2 
 SCRAPE_URL = 'https://sg.finance.yahoo.com/markets/stocks/gainers/'
 a stock profit table


 ## Stage5
 # DATA STORAGE
 - Env-driven paths(C:\Users\go199\Desktop\PY) to `data/raw/` and `data/processed/`
- Save CSV and Parquet; reload and validate
- Abstract IO with utility functions; document choices
# Validation
{'shape_equal': True, 'date_is_datetime': True, 'price_is_numeric': True}