import pandas as pd
import numpy as np

df = pd.read_csv("cleaned_data.csv")
print(df.head())
area_group = df.groupby("area")

# Total salary by area
area_salary_sum = area_group["salary"].sum()
print(area_salary_sum)

# Max revenue by area
area_revenue_max = area_group["revenue"].max()
print(area_revenue_max)

group_type_grp = df.groupby("group_type")

# Average salary per group type
avg_salary = group_type_grp["salary"].mean()
print(avg_salary)

# CONDITIONAL FILTERING (single + multiple conditions)
high_salary = df[df["salary"] > 60000]
print(high_salary)


# GROUPBY + FILTER COMBINATION
filtered_data = df[
    (df["gender"] == "Male") &
    (df["age_years"] < 30)
]
print(filtered_data)

area_grp = df.groupby("area")
specific_area = area_grp.get_group(df["area"].unique()[0])
total_units = specific_area["units"].sum()
print(total_units)

# CREATE NEW COLUMN
df["total_value"] = df["units"] * df["revenue"]
print(df[["units", "revenue", "total_value"]])

# MULTI-LEVEL GROUPBY (VERY IMPORTANT)
multi_grp = df.groupby(["area", "gender"])
multi_result = multi_grp["salary"].mean()
print(multi_result)

# ADVANCED FILTER + GROUPBY
result = df[
    (df["employment_status"] == "Contract") &
    (df["salary"] > df["salary"].median())
]
print(result)

# PIVOT TABLE
# Pivot 1: Single index
pivot_1 = df.pivot_table(
    values="salary",
    index="gender",
    aggfunc=["mean", "sum"]
)
print(pivot_1)
# Pivot 2: Multiple index
pivot_2 = df.pivot_table(
    values="revenue",
    index=["area", "employment_status"],
    aggfunc=["sum", "max"]
)
print(pivot_2)
# Pivot 3: Multiple values + aggregation
pivot_3 = df.pivot_table(
    values=["salary", "units"],
    index="group_type",
    aggfunc={"salary": "mean", "units": "sum"}
)
print(pivot_3)

# DATE-BASED OPERATION
df["join_year"] = pd.to_datetime(df["join_date"]).dt.year

year_grp = df.groupby("join_year")["salary"].mean()
print(year_grp)