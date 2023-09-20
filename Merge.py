import os
import pandas as pd
import concurrent.futures

# Get the current working directory
current_directory = os.getcwd()

# Get a list of all CSV files in the current directory
csv_files = [f for f in os.listdir(current_directory) if f.endswith('.csv')]

# Initialize an empty DataFrame to store the merged data
merged_data = pd.DataFrame()

# Loop through each CSV file and merge it into the DataFrame
for csv_file in csv_files:
    file_path = os.path.join(current_directory, csv_file)
    data = pd.read_csv(file_path)
    merged_data = pd.concat([merged_data, data], ignore_index=True)

# Save the merged data to a new CSV file
merged_data.to_csv('merged_data.csv', index=False)

print('CSV files merged successfully!')
