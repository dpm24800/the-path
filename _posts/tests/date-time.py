import pandas as pd

# Create DataFrame
df = pd.DataFrame({
    'Date': ['2024-01-15', '2024-02-20', '2024-03-10'],
    'Sales': [1000, 1500, 1200]
})

# Convert Date to datetime and split into Year, Month, Day
df['Date'] = pd.to_datetime(df['Date'])
df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month
df['Day'] = df['Date'].dt.day

print(df)