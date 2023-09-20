import os
import pandas as pd
import concurrent.futures

# Get the list of CSV files in the directory
csv_files = [filename for filename in os.listdir('.') if filename.endswith('.csv')]

# Process each CSV file
for csv_file in csv_files:
    print(f"Processing {csv_file}...")

    # Read the CSV file
    df = pd.read_csv(csv_file)

    # Create a dictionary to store data for each PIN
    output_data = {}

    # Process each row
    for i, row in df.iterrows():
        a_value = row['PIN']
        key_value = row['Key']
        test_name_value = row['TestName']
        value = row['Value']

        if key_value in ['ResponseTime', 'Score']:
            column_name = f'{test_name_value}_{row["ItemID"]}_{key_value}'
            if a_value not in output_data:
                output_data[a_value] = {'A': a_value}
            output_data[a_value][column_name] = value

    # Create a new DataFrame from the processed data
    new_df = pd.DataFrame.from_dict(output_data, orient='index')

    # Set the first cell in column A to the same value as in the first data row
    if not new_df.empty:
        new_df.iloc[0, new_df.columns.get_loc('A')] = new_df.index[0]

    # Write the new DataFrame to an Excel file with a name based on the CSV file name
    excel_file = os.path.splitext(csv_file)[0] + '_output.xlsx'
    new_df.to_excel(excel_file, index=False)

    print(f"Finished processing {csv_file}. Output saved as {excel_file}\n")




