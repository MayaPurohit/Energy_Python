import pandas as pd
import json

# Specify the input and output file paths
input_file = "tasks.jsonl"  # Replace with your JSONL file

# Read the JSONL file
data = []
with open(input_file, 'r') as file:
    for line in file:
        data.append(json.loads(line))


df = pd.DataFrame(data)

execution = df['execution'].to_list()
new_data = []


for i in range(len(execution)):
    new_data.append(json.loads(json.dumps(execution[i])))

final = pd.DataFrame(new_data).to_numpy()
print(final.shape)

initial_time = final[0,1]
final[:, 1:] = final[:, 1:] - initial_time
print(final)