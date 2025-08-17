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