
import pandas as pd

# Load the dataset
df = pd.read_csv('titanic.csv')

# Filter the data to include only the rows where the 'Survived' column is 1 (indicating survival)
survived_df = df[df['Survived'] == 1]

# Save the filtered data to a new CSV file
survived_df.to_csv('survived.csv', index=False)

print('Survivor information has been saved to survived.csv')
