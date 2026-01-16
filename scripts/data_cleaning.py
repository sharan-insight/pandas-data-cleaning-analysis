import pandas as pd

# Load
emp = pd.read_csv("raw_data.csv")

# Rename columns (like your example)
emp.rename(
    columns={
        "person_name": "name","uid": "employee_id","work_status": "employment_status",
        "sex": "gender","start_dt": "join_date","pay_amount": "salary"},inplace=True)

# Rearrange columns
# Keep all columns but order them in a sensible way
desired_order = ["employee_id","name","area","group_type","sub_group","gender","age_years","salary",
                 "units","revenue","employment_status","join_date","ref_dt","extra_col"]
desired_order = [c for c in desired_order if c in emp.columns]
emp = emp[desired_order]

# Map gender (male/female to M/F)
emp["gender"] = (emp["gender"].astype("string").str.strip().str.capitalize())

# Strip spaces in name
emp["name"] = emp["name"].astype("string").str.strip()

# Fill missing values + datatype changes
# age_years: fill with mean then convert to integer type
emp["age_years"] = pd.to_numeric(emp["age_years"], errors="coerce")
age_mean = emp["age_years"].mean(skipna=True)
emp["age_years"] = emp["age_years"].fillna(age_mean)
emp["age_years"] = emp["age_years"].round().astype("Int64")

# employment_status: fill missing with 'contract'
emp["employment_status"] = emp["employment_status"].astype("string")
emp["employment_status"] = emp["employment_status"].fillna("contract")

# salary: fill missing with median
emp["salary"] = pd.to_numeric(emp["salary"], errors="coerce")
salary_median = emp["salary"].median(skipna=True)
emp["salary"] = emp["salary"].fillna(salary_median)

# join_date: parse date and forward fill
emp["join_date"] = pd.to_datetime(emp["join_date"], errors="coerce", dayfirst=True)
emp["join_date"] = emp["join_date"].fillna(method="ffill")

# ref_dt: parse date too
emp["ref_dt"] = pd.to_datetime(emp["ref_dt"], errors="coerce", dayfirst=True)

# Drop duplicates
emp.drop_duplicates(inplace=True)

# Normalize text formatting (capitalize employment_status)
emp["employment_status"] = emp["employment_status"].astype("string").str.strip().str.capitalize()

# Drop an unwanted column (your example drops exp_years; here we drop extra_col)
emp.drop(["extra_col"], axis=1, inplace=True)

# Reset index, drop old index column
emp.reset_index(inplace=True)
emp.drop(["index"], axis=1, inplace=True)

# Save cleaned data
emp.to_csv("cleaned_data.csv", index=True)

print(emp)