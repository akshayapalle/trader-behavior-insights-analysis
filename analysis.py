import pandas as pd

# Load datasets
fear_greed = pd.read_csv("fear_greed_index.csv")
trades = pd.read_csv("historical_data.csv")

# Convert date columns to proper datetime format
fear_greed['date'] = pd.to_datetime(fear_greed['date']).dt.date
trades['Timestamp IST'] = pd.to_datetime(trades['Timestamp IST'], format='%d-%m-%Y %H:%M')
trades['date'] = trades['Timestamp IST'].dt.date

# Merge datasets on date to align trades with market sentiment
merged = pd.merge(trades, fear_greed, on='date', how='inner')

# Preview merged data
print(merged.head())
print("Rows:", len(merged))

# Calculate average profit (Closed PnL) for each sentiment category
profit_by_sentiment = merged.groupby('classification')['Closed PnL'].mean()

print("\nAverage Profit by Sentiment:")
print(profit_by_sentiment)

# Calculate average trade size (USD) for each sentiment category
size_by_sentiment = merged.groupby('classification')['Size USD'].mean()

print("\nAverage Trade Size by Sentiment:")
print(size_by_sentiment)

import matplotlib.pyplot as plt

# Visualize average profit by market sentiment
profit_by_sentiment.plot(kind='bar')
plt.title("Average Profit by Market Sentiment")
plt.ylabel("Avg Closed PnL")
plt.show()