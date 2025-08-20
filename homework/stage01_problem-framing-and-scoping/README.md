# Project Title
**Stage:** Problem Framing & Scoping (Stage 01)
## Problem Statement
This project is focused on applying various applicable Machine Learning algorithms to predict the stock prices of the top 5 largest publically trading U.S. companies by market capital utilizing historic data obtained from Yahoo Finance. Specifically, NVIDIA, Microsoft, Apple, Alphabet, and Amazon. 

The movements of these 5 companies are important as they represent around 25% of the entire U.S. market and as such, significantly affect the market as a whole. We hope to be able to utilize these movements to inform trades in the broader market. Data Sourced from: https://companiesmarketcap.com/usa/largest-companies-in-the-usa-by-market-cap/ and metrics quoted on August 16th, 2025. 
## Stakeholder & User
The key decision owner is our firm's portfolio manager and the users will be the portfolio manager, analysts, and quants who work at the desk for trading shares in domestic markets. 
## Useful Answer & Decision
Our models will be predictive and designed to forecast prices. Confidence bands will be built in to account for risk. The metric will be the forecasted share prices for the top 5 U.S. companies. 
## Assumptions & Constraints
We assume stationarity due to time series analysis, liquidity in the market, and stability. 

We have constraints in that we have limited computational power needed to create our model as well as compliance-related restrictions. 
## Known Unknowns / Risks
- Model Stability through stress scenarios
- Black Swan events causing major market disruptions
- Regulatory bodies reaction and interference with our model
## Lifecycle Mapping
Define stakeholder problem → Stage 01 (Problem Framing & Scoping) → Scoping paragraph, stakeholder memo


## Repo Plan
/data/ - for raw/processed data
/src/ - for reusable functions and scripts
/notebooks/ - for jupyter notebooks displaying python code
/docs/ for memos, personas, design notes, and other relevant information



