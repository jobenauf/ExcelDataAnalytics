import pandas as pd

# Read the CSV file
df = pd.read_csv('2020-03-13-17.31.48-NS-Data.csv')

# Create a new DataFrame to store the output
new_df = pd.DataFrame(columns=['A', 'B', 'C'])

# Find all rows where the value in column 'Key' is 'Score'
score_rows = df[df['Key'] == 'Score']

# Process each row
for i, row in score_rows.iterrows():
    # Get the values from columns A, E, and Key
    a_value = row['PIN']
    e_value = row['ItemID']
    key_value = row['Key']

    # Add the values to the new DataFrame
    new_df = new_df.append({'A': a_value, 'B': f'{key_value}_{e_value}'}, ignore_index=True)

# Find all rows where the value in column 'Key' is 'ResponseTime'
response_time_rows = df[df['Key'] == 'ResponseTime']

# Process each row
for i, row in response_time_rows.iterrows():
    # Get the value from column K
    k_value = row['Value']

    # Add the value to the new DataFrame
    new_df.loc[i, 'C'] = k_value

# Write the new DataFrame to an Excel file
new_df.to_excel('output.xlsx', index=False)



