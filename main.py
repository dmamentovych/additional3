import pandas as pd

file_path = 'supermarket_sales.csv'
df = pd.read_csv(file_path)

# print(df.head())
#
print(df.isnull().sum())

df.dropna(inplace=True)

df['Date'] = pd.to_datetime(df['Date'])
df['Unit price'] = df['Unit price'].astype(float)
df['Quantity'] = df['Quantity'].astype(int)
df['Tax 5%'] = df['Tax 5%'].astype(float)
df['Total'] = df['Total'].astype(float)
df['cogs'] = df['cogs'].astype(float)
df['gross income'] = df['gross income'].astype(float)
df['Rating'] = df['Rating'].astype(float)

# data_types = df.dtypes

# print(data_types)

summary_stats = df.describe()
total_sales = df['Total'].sum()

average_sales = df.resample('ME', on='Date')['Total'].sum().mean()
max_sales = df['Total'].max()
min_sales = df['Total'].min()

unique_values = {
    'Product line': df['Product line'].nunique(),
    'Branch': df['Branch'].nunique(),
    'City': df['City'].nunique(),
    'Customer type': df['Customer type'].nunique(),
    'Gender': df['Gender'].nunique(),
    'Payment': df['Payment'].nunique()
}

categorical_stats = df[['Product line', 'Branch', 'City', 'Customer type', 'Gender', 'Payment']].value_counts()
print(summary_stats, total_sales, average_sales, max_sales, min_sales, unique_values, categorical_stats)

df['Profit Margin'] = df['gross income'] / df['cogs'] * 100
monthly_sales = df.resample('ME', on='Date')['Total'].sum()
monthly_sales_growth = monthly_sales.pct_change().fillna(0) * 100
sales_by_product_category = df.groupby('Product line')['Total'].sum()
sales_by_product_category_percentage = (sales_by_product_category / total_sales) * 100
top_products_by_sales_volume = df.groupby('Product line')['Total'].sum().sort_values(ascending=False).head(5)

print(monthly_sales_growth, sales_by_product_category, top_products_by_sales_volume)
