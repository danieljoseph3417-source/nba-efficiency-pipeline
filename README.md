# NBA Efficiency Analysis Pipeline 🏀

## Overview
This project is an automated ETL (Extract, Transform, Load) pipeline built with **Python** and **Pandas**. It ingests raw NBA player data, cleans inconsistencies, engineers financial metrics, and determines which teams are spending their salary cap most efficiently.

## Key Features
* **Data Ingestion:** Reads raw CSV data simulating an external API feed.
* **Data Cleaning:** automated handling of missing values (NaN) and duplicate records.
* **Feature Engineering:** Calculates `Cost_Per_Point` to normalize salary efficiency.
* **Aggregations:** Groups data by Team to derive organization-level insights.

## Technologies Used
* Python 3.x
* Pandas (DataFrames, GroupBy, Vectorized Math)
* CSV I/O

## How to Run
1. Run `generate_data.py` to simulate the raw data feed.
2. Run `pipeline.py` to execute the transformation and generate the final report.
