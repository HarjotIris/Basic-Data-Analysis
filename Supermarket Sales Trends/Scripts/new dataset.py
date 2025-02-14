import pandas as pd

# Load the dataset
file_path = r"C:\Desktop\PRACTICE\SALE TRENDS\supermarket_sales - Sheet1.csv"
df = pd.read_csv(file_path)

# Show basic info
print(df.info())
print(df.head())

print(df.isnull().sum())

df_columns = df.columns.str.strip()

df['Date'] = pd.to_datetime(df['Date'])
df.sort_values(by='Date', inplace=True)

df['Time'] = pd.to_datetime(df['Time'], format = '%H:%M').dt.time
df['Total'] = df['Total'].astype(float)  # Ensure 'Total' column is numeric

# General Statistics
print(df.describe()) # Summary statistics for numerical columns

print(df.describe(include='object')) # Summary statistics for categorical columns


# Unique values in Categorical Columns
for col in ['Branch', 'City', 'Customer type', 'Gender', 'Product line', 'Payment']:
    print(f"{col} unique values: {df[col].unique()}\n")

import matplotlib.pyplot as plt

# Group by date and sum total sales
df_daily_sales= df.groupby('Date')['Total'].sum()

# Sale Trends over Time
plt.figure(figsize = (12, 5))
plt.plot(df_daily_sales.index, df_daily_sales.values, marker = 'o', linestyle = '-')
plt.xlabel("Date")
plt.ylabel("Total Sales")
plt.title("Daily Sales Trend")
plt.xticks(rotation = 45)
plt.grid()
plt.show()

import seaborn as sns

# Total by City
plt.figure(figsize=(8, 5))
sns.barplot(x = df['City'], y = df['Total'], estimator=sum)
plt.xlabel("City")
plt.ylabel("Total Sales")
plt.title("Total Sales by City")
plt.show()

# Most Popular Payment Method
plt.figure(figsize=(6, 5))
sns.countplot(x = df['Payment'], order = df['Payment'].value_counts().index)
plt.xlabel("Payment Method")
plt.ylabel("Count")
plt.title("Most Used Payment Methods")
plt.show()


# Ensure 'Date' is in datetime format
df['Date'] = pd.to_datetime(df['Date'])
df.sort_values(by='Date', inplace=True)

# Compute rolling average for total sales per day
df_daily_sales = df.groupby('Date')['Total'].sum()
daily_sales_7 = df_daily_sales.rolling(window=7).mean()
daily_sales_30 = df_daily_sales.rolling(window=30).mean()

# Plot rolling average
plt.figure(figsize=(12, 5))
plt.plot(df_daily_sales.index, df_daily_sales, label='Daily Sales', alpha=0.5)
plt.plot(df_daily_sales.index, daily_sales_7, label='7-Day Rolling Avg', color='red')
plt.plot(df_daily_sales.index, daily_sales_30, label='30-Day Rolling Avg', color='green')
plt.xlabel('Date')
plt.ylabel('Total Sales')
plt.title('Daily Sales Trend with Rolling Averages')
plt.legend()
plt.xticks(rotation=45)
plt.grid()
plt.show()

# Correlation Analysis
correlation_matrix = df[['Total', 'Quantity', 'gross income', 'Rating']].corr()
print("\nCorrelation Matrix:\n", correlation_matrix)
