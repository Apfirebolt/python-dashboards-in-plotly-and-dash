import pandas as pd

df = pd.read_csv('../data/hdfc.csv')

# Converts the entire dataframe into string

print(df.to_string())

data_header = df.head() 

print(data_header)

# Columns
print(df.columns)
print(list(df.columns.values))

print('Highest Value HDFC ', df['Open'].max())
print('Lowest Value HDFC ', df['Open'].min())
print('Mean Value HDFC ', df['Open'].mean())

# Information related to dataframe like how large dataframe is, rows and columns and more.

print(df.info())
print(df.describe())

# Filtering dataframes, select values with Open price > 2200

filtered_df = df[df['Open'] > 2200]
# Only print Open and Volume column data for filtered dataframe

print(df[['Open','Volume']].head())

# Sorting by a specific column values

print(filtered_df.sort_values(['Volume']).tail())

# Print values in a given range using slicing

print(df['Open'][3:17])