
import pandas as pd

# Load the dataset
df = pd.read_csv('organizations-100.csv')

# Sort the DataFrame by the 'Number of employees' column
sorted_df = df.sort_values(by='Number of employees', ascending=True)

# Save the sorted data to a new CSV file
sorted_df.to_csv('sorted_csv.csv', index=False)

print('Sorted information has been saved to sorted_csv.csv')
