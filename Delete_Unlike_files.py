import os
import glob

# Get a list of all files ending with "output.xlsx" in the current directory
files_to_remove = glob.glob('output.xlsx')

# Remove each file in the list
for file in files_to_remove:
    try:
        os.remove(file)
        print(f"Removed {file}")
    except OSError as e:
        print(f"Error removing {file}: {e}")

print("Done removing files ending with 'output.xlsx'")

