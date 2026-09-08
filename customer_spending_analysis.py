"""
Mini Project: Customer Spending Analysis
Author: Hamsa Adel
Purpose: A beginner-friendly Data Science project covering data loading,
cleaning, exploratory data analysis, visualization, and simple insights.
"""

import pandas as pd
import matplotlib.pyplot as plt

# ---------------------------------------------------------
# 1. Load the dataset
# ---------------------------------------------------------
df = pd.read_csv("customer_spending.csv")

print("First 5 rows:")
print(df.head())

# ---------------------------------------------------------
# 2. Understand the dataset
# ---------------------------------------------------------
print("\nDataset shape:", df.shape)
print("\nData types:")
print(df.dtypes)
print("\nMissing values:")
print(df.isnull().sum())

# ---------------------------------------------------------
# 3. Clean missing values
# Numeric columns -> median
# Categorical columns -> mode
# ---------------------------------------------------------
numeric_cols = ["Annual_Income", "Satisfaction_Score"]
categorical_cols = ["City"]

for col in numeric_cols:
    df[col] = df[col].fillna(df[col].median())

for col in categorical_cols:
    df[col] = df[col].fillna(df[col].mode()[0])

print("\nMissing values after cleaning:")
print(df.isnull().sum())

# ---------------------------------------------------------
# 4. Descriptive statistics
# ---------------------------------------------------------
print("\nDescriptive statistics:")
print(df.describe())

# ---------------------------------------------------------
# 5. Create a useful feature: Average Order Value
# ---------------------------------------------------------
df["Average_Order_Value"] = df["Annual_Spending"] / df["Orders"].replace(0, 1)

# ---------------------------------------------------------
# 6. Group analysis
# ---------------------------------------------------------
city_spending = (
    df.groupby("City")["Annual_Spending"]
      .mean()
      .sort_values(ascending=False)
)

print("\nAverage spending by city:")
print(city_spending)

# ---------------------------------------------------------
# 7. Correlation analysis
# ---------------------------------------------------------
corr = df[[
    "Annual_Income",
    "Website_Visits",
    "Orders",
    "Satisfaction_Score",
    "Annual_Spending"
]].corr()

print("\nCorrelation matrix:")
print(corr["Annual_Spending"].sort_values(ascending=False))

# ---------------------------------------------------------
# 8. Visualizations
# ---------------------------------------------------------
plt.figure(figsize=(8, 5))
plt.scatter(df["Annual_Income"], df["Annual_Spending"], alpha=0.7)
plt.xlabel("Annual Income")
plt.ylabel("Annual Spending")
plt.title("Income vs Annual Spending")
plt.tight_layout()
plt.savefig("income_vs_spending.png", dpi=150)
plt.show()

plt.figure(figsize=(8, 5))
city_spending.plot(kind="bar")
plt.xlabel("City")
plt.ylabel("Average Annual Spending")
plt.title("Average Spending by City")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("spending_by_city.png", dpi=150)
plt.show()

# ---------------------------------------------------------
# 9. Key business-style insights
# ---------------------------------------------------------
top_city = city_spending.index[0]
top_city_value = city_spending.iloc[0]
income_corr = corr.loc["Annual_Income", "Annual_Spending"]
orders_corr = corr.loc["Orders", "Annual_Spending"]

print("\nKEY INSIGHTS")
print(f"1. {top_city} has the highest average annual spending: {top_city_value:,.2f}.")
print(f"2. Income-to-spending correlation: {income_corr:.2f}.")
print(f"3. Orders-to-spending correlation: {orders_corr:.2f}.")
print("4. Missing numeric values were handled using the median, while categorical")
print("   missing values were handled using the most frequent category.")
