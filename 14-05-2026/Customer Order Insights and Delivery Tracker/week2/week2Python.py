import pandas as pd
import numpy as np

# LOAD DATA

df = pd.read_csv("orders.csv")

print("original data")
print(df)

# CHECK MISSING VALUES

print("\nmissing values")
print(df.isnull().sum())


# HANDLE MISSING VALUES
# Fill missing delivery_date with current date
df['delivery_date'] = df['delivery_date'].fillna(pd.Timestamp.today().strftime('%Y-%m-%d'))


# CONVERT DATE COLUMNS

df['order_date'] = pd.to_datetime(df['order_date'])
df['delivery_date'] = pd.to_datetime(df['delivery_date'])


# CALCULATE DELIVERY DAYS
df['delivery_days'] = (df['delivery_date'] - df['order_date']).dt.days

# CALCULATE DELAY
# Assume >5 days = delayed

df['delayed'] = np.where(df['delivery_days'] > 5, 1, 0)

# SHOW CLEANED DATA
print("\nCLEANED DATA")
print(df)


# TOP DELAYED CUSTOMERS
top_delayed = df.groupby('customer_name')['delayed'].sum().sort_values(ascending=False)

print("\nTop delayed customers")
print(top_delayed)

# MOST COMMON DELIVERY ISSUES

common_issues = df['issue'].value_counts()

print("\ncommon delivery issue")
print(common_issues)


# SAVE CLEANED DATA

df.to_csv("cleaned_orders.csv", index=False)

print("\nCleaned dataset saved successfully")