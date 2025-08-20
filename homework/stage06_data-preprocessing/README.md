# Project Title
# Problem Framing & Scoping (Stage 01)
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


# Data Storage(Stage 05)
## Problem Statement
This stage of the project is concerned with the ability to store raw and processed data files in accurate and replicable locations.
## Stakeholder & User
Stakeholder and users will be individuals who need to access the data in order to create the models
## Useful Answer & Decision
The data storage process must ensure that both raw and processed datasets are stored in a centralized, well-documented location that supports real-time or scheduled updates. This enables consistent access for stakeholders and allows for reproducibility.
## Assumptions & Constraints
We assume that data remains in the designated location
We assume that future updates to data are compatible with existing structure
Storage must comply with regulatory requirements
Access permissions must be strictly enforced to prevent unauthorized use
## Known Unknowns / Risks
- Data integrity risks - accidental deletion, overwrite, corruption
- Storage performance - large datasets could significantly slow down access
- Regulatory bodies - compliance with regulations in our data storage practices
## Lifecycle Mapping
Design storage structure → Stage 05 (Data Storage) → Implement centralized, secure storage


# Data Preprocessing (Stage 06)

## Problem Statement
This stage of the project focuses on preparing raw datasets for analysis and modeling by applying cleaning and preprocessing steps. The goal is to ensure that datasets are free of excessive missing values, have imputed replacements where appropriate, and are standardized for consistent downstream use.

## Stakeholder & User
Stakeholders and users are data analysts, data scientists, and engineers who require clean, consistent data for model development and analysis. They rely on preprocessing to remove inconsistencies and prepare features in a format suitable for modeling.

## Useful Answer & Decision
The preprocessing step applies a sequence of data cleaning operations:
- Filling missing numeric values with the median of non-missing entries.
- Dropping rows with missing values exceeding a user-defined threshold.
- Standardizing numeric columns to have zero mean and unit variance.

This ensures that datasets are consistent, handle missingness appropriately, and are numerically prepared for model algorithms that assume normalized inputs.

## Assumptions & Constraints

- Missing values can be removed or imputed without losing significant information.
- StandardScaler() assumes the data is approximately normally distributed; deviations from this may require alternative scaling.
- Excessive row removal due to missing values can bias or reduce the dataset’s representativeness.
- Future datasets must follow the same schema and formatting to be compatible with these preprocessing steps.

## Known Unknowns / Risks

- The true reason for missing values may carry meaning that is lost during imputation.
- Applying median imputation may not be suitable for skewed distributions.
- Removing too many rows may cause loss of important patterns or introduce sampling bias.
- Preprocessing steps may need adjustment if future datasets differ in structure or data type distributions.

## Lifecycle Mapping

Load raw dataset → Apply cleaning functions ) → Validate results → Save cleaned dataset to data/processed/ for downstream modeling.

