import pandas as pd
import json
import numpy as np
import plot_data
import matplotlib.pyplot as plt 
from scipy.linalg import lstsq
import scipy.integrate

def parse_json(filename):

    input_file = filename 


    data = []
    with open(input_file, 'r') as file:
        for line in file:
            data.append(json.loads(line))


    df = pd.DataFrame(data)

    execution = df['execution'].to_list()
    new_data = []


    for i in range(len(execution)):
        new_data.append(json.loads(json.dumps(execution[i])))

    final = pd.DataFrame(new_data)
    
    initial_time = final.iloc[0,3]
    final.iloc[:, 1:] = final.iloc[:, 1:] - initial_time
    final.iloc[:, 0] = np.array(range(1, final.shape[0]+1), dtype = str)

    final.iloc[:, 0] = "Task " + final.iloc[:, 0]
    final["task_duration"] = final["task_end_time"] - final["task_start_time"]
    final["input_duration"] = final["input_transform_end_time"] - final["input_transform_start_time"]
    final["result_duration"] = final["result_transform_end_time"] - final["result_transform_start_time"]
    return final



def plot_gantt(json_file, energy_file, workflow_type, byte_size):

    task_data = parse_json(json_file)


    prepped_data = plot_data.prep_data(fr"C:\Users\mayam\Energy_Python\{energy_file}", "ipmi", "write")


    fig,ax = plt.subplots(nrows = 2, ncols = 1, sharex=True, figsize = (10,15), gridspec_kw={'height_ratios': [0.5, 4]})
    ax[0].plot(prepped_data[:, 3], prepped_data[:, 2])
    ax[0].set_title("Energy Measurement for " + workflow_type + " Tasks (10^" + str(byte_size) + ") bytes")
    # ax[1].set_yticks(np.arange(task_data.shape[0]))
    # ax[1].set_yticklabels(task_data["hostname"])
    # ax[1].set_xticks(range(0,310,10))
    ax[1].set_xlabel("Time (seconds)")
    for i in range(task_data.shape[0]):
        if i == 0:
            ax[1].barh(i-0.2, task_data.loc[i, "task_duration"], left=task_data.loc[i, "task_start_time"], height=0.2, color = "r", align='center', label = "Task Duration")
            ax[1].barh(i, task_data.loc[i, "input_duration"], left=task_data.loc[i, "input_transform_start_time"], height=0.2, color = "g", align='center', label = "Input Transform")
            ax[1].barh(i+0.2, task_data.loc[i, "result_duration"], left=task_data.loc[i, "result_transform_start_time"], height=0.2, color = "b", align='center', label = "Result Transform")
        else:
            ax[1].barh(i-0.2, task_data.loc[i, "task_duration"], left=task_data.loc[i, "task_start_time"], height=0.2, color = "r", align='center')
            ax[1].barh(i, task_data.loc[i, "input_duration"], left=task_data.loc[i, "input_transform_start_time"], height=0.2, color = "g", align='center')
            ax[1].barh(i+0.2, task_data.loc[i, "result_duration"], left=task_data.loc[i, "result_transform_start_time"], height=0.2, color = "b", align='center')
    plt.legend()
    plt.show()


prepped_data = plot_data.prep_data(fr"C:\Users\mayam\Energy_Python\{energy_file}", "ipmi", "write")

area = scipy.integrate.simpson(prepped_data[:, 3], x = prepped_data[:, 2])

plot_gantt("bag_8_daos.jsonl", "ipmi_bag_8_daos.csv", "bag", 8)


