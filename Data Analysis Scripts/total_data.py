import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
import pandas as pd
import plot_data
# from scipy.linalg import lstsq



def plot_total(nodes, iotype, idle_consideration = False):
    types = ["ipmi"]
    fig = plt.subplots(figsize =(8.7, 5)) 
    allVals = []

    for node in nodes:
        for i in range(len(types)):
                if types[i] == "turbostat":
                        xVal = 2
                        yVal = 1
                elif types[i] == "powerstat":
                        if node == "nvme1" or  node == "nvme2":
                                xVal = 21
                        elif node == "admin":
                                xVal = 26
                        else:
                                xVal = 23
                        yVal = 12
                else:
                        xVal = 3
                        yVal = 2

                filename = types[i] + "_" + node + "_" + iotype + ".csv"
                print(filename)
                prepped = plot_data.prep_data(fr"C:\Users\mayam\OneDrive\Desktop\BigDataX\Week5\{node}\{types[i]}\{filename}", types[i], iotype,  node, idle_consideration)
                # if types[i] == "powerstat":
                #       for j in range(prepped.shape[0]-1):
                #             if prepped[j + 1, 26] != prepped[j, 26] + 1 and prepped[j + 1, 26] != prepped[j, 26] + 2:
                #                 print("Index", j)
                #                 print("second", prepped[j + 1, 26])
                #                 print("time: ", prepped[j + 1, 0])
                #                 print("first", prepped[j, 26])
                #                 print("time: ", prepped[j, 0])

                # print(prepped[:, xVal].shape)
                if types[i] == "ipmi":
                        plt.plot(prepped[:, xVal], prepped[:, yVal], label =node.capitalize() + " Power")
                #     idle = np.ones([prepped[:, xVal].shape[0], 1]) * 207.8975741
                #     plt.plot(np.reshape(prepped[:, xVal], [prepped[:, xVal].shape[0], 1]), idle)
                elif types[i] =="powerstat":
                        plt.plot(prepped[:, xVal], prepped[:, yVal], label ="CPU Power Measurements")
                else:
                        plt.plot(prepped[:, xVal], prepped[:, yVal], label ="RAM Measurements") 
                
                allVals.append(prepped[:, [xVal, yVal]])

#     smaller = min(allVals[1].shape[0], allVals[0].shape[0])
#     print(allVals[1].shape[0],  allVals[0].shape[0])
#     print(allVals[0][allVals[0][:, 0] < smaller])
#     sum = allVals[1][allVals[1][:, 0] < smaller][:, 1] + allVals[0][allVals[0][:, 0] < smaller][:, 1]

#     plt.plot(allVals[1][allVals[1][:, 0] < smaller][:, 0], sum, label = "CPU + RAM")

    plt.ylabel("Power (Watts)")
    plt.xlabel("Time Elasped (seconds)")
#     plt.yticks(range(0,230, 30))
#     plt.xticks(range(0,90,10))
#     plt.title(node.capitalize() + " Power Analysis (" + iotype.capitalize() + ")")
    plt.legend(bbox_to_anchor=(1.35, 0.7), loc = "center right",)
    plt.tight_layout()
    plt.show()




plot_total(["admin", "nvme1", "nvme2"], "write", False)



