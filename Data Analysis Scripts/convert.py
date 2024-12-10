import pandas as pd
import json

# Specify the input and output file paths
input_file = "your_file.jsonl"  # Replace with your JSONL file
output_file = "output_file.xlsx"  # Replace with your desired Excel file name

# Read the JSONL file
data = []
with open(input_file, 'r') as file:
    for line in file:
        data.append(json.loads(line))

# Convert to DataFrame
df = pd.DataFrame(data)

# Write to Excel
df.to_excel(output_file, index=False, engine='openpyxl')

print(f"JSONL file has been converted to {output_file}")
