📊 Pandas Data Cleaning and Analysis Project
📌 Overview

This project focuses on end-to-end data processing using Python and Pandas.
It starts with a raw CSV dataset, applies systematic data cleaning techniques, and then performs data analysis using grouping, filtering, and pivot tables.

🧹 Data Cleaning Process
-The following cleaning operations were performed:
-Renamed columns for better readability
-Reordered columns logically
-Removed extra spaces from text fields
-Standardized categorical values (gender, employment status)
-Handled missing values using:
-Mean for age
-Median for salary
-Forward fill for dates
-Converted columns to proper data types
-Removed duplicate records
-Dropped unnecessary columns
-Reset index after cleaning
-Exported cleaned data to a new CSV file

📈 Data Analysis Performed
-Using the cleaned dataset, the following analyses were completed:
-GroupBy aggregations (sum, mean, max)
-Conditional filtering (single and multiple conditions)
-Multi-level GroupBy analysis
-Creation of derived columns
-Pivot tables with multiple aggregations
-Date-based analysis (year-wise trends)
-These operations reflect real-world business data analysis tasks.

🛠 Technologies Used
-Python
-Pandas
-CSV files

▶ How to Run the Project
1. Install dependencies
pip install -r requirements.txt
2. Run data cleaning
python scripts/data_cleaning.py
3. Run data analysis
python scripts/data_analysis.py