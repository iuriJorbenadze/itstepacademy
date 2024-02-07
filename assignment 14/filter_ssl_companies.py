
import pandas as pd

# Load the dataset
df = pd.read_csv('organizations-100.csv')

# Filter the data to include only rows where the 'Website' column starts with 'https://'
ssl_df = df[df['Website'].str.startswith('https://')]

# Select only specified columns
ssl_df = ssl_df[['Organization Id', 'Name', 'Website', 'Industry', 'Number of employees']]

# Save the filtered data to a new CSV file
ssl_df.to_csv('ssl_companies.csv', index=False)

print('SSL protected companies information has been saved to ssl_companies.csv')
