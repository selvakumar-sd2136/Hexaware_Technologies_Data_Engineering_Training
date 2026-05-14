import pandas as pd
import numpy as np

# Load CSV
df = pd.read_csv("week2_Orders.csv")

print("Original Data")
print(df)

# Remove null values
df = df.dropna()

# Convert to datetime
df['delivery_date'] = pd.to_datetime(df['delivery_date'])

# Calculate delay
today = pd.Timestamp("2026-01-20")

df['delay_days'] = (
    today - df['delivery_date']
).dt.days

# Delayed or not
df['is_delayed'] = np.where(
    df['delay_days'] > 5,1,0
)

print("\nProcessed Data")
print(df)