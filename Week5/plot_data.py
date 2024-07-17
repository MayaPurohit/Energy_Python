import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
import pandas as pd
import sys
# from scipy.linalg import lstsq


def prep_data(filename, type):
    if type == "turbostat":
        storageVals = pd.read_csv(filename, delimiter =r'\s+').to_numpy()
        storageVals = storageVals.astype(str)

        condition1 = storageVals[:, 1] != "nan"
        condition2 = storageVals[:, 1] != "RAMWatt"
        combined_condition = condition1 & condition2
        storageVals = storageVals[combined_condition]
        storageVals = np.asfarray(storageVals)
        storageVals = storageVals[::3]

        initial_time = storageVals[0,0]
        time_elapsed = np.zeros([storageVals.shape[0], 1])

        for i in range(storageVals.shape[0]):
            time_elapsed[i] = int(storageVals[i,0] - initial_time)

        totalVals = np.hstack((storageVals, time_elapsed))

    elif type == "powerstat":
        storageVals = pd.read_csv(filename, delimiter =r'\s+').to_numpy()

        storageVals = storageVals[storageVals[:,0] != "Time"]
        storageVals[:,0] = "2024-07-06 " + storageVals[:, 0] 

        time_format = '%Y-%m-%d %H:%M:%S'

        time_elapsed = np.zeros([storageVals.shape[0], 1])
        initial_time = datetime.strptime(storageVals[0,0], time_format)
        print(initial_time)
        initial_time = int(initial_time.timestamp())

        for i in range(storageVals.shape[0]):
            timeNum = datetime.strptime(storageVals[i,0], time_format)
            time_int = int(timeNum.timestamp())
            time_elapsed[i] = (time_int - initial_time)

        totalVals = np.hstack((storageVals, time_elapsed))
        totalVals[:, 12] = np.asfarray(totalVals[:,12])

    else:
        storageVals = pd.read_csv(filename).to_numpy()
        time_format = '%Y-%m-%d %H:%M:%S'

        time_elapsed = np.zeros([storageVals.shape[0], 1])
        initial_time = datetime.strptime(storageVals[0,0], time_format)
        initial_time = int(initial_time.timestamp())

        for i in range(storageVals.shape[0]):
            timeNum = datetime.strptime(storageVals[i,0], time_format)
            time_int = int(timeNum.timestamp())
            time_elapsed[i] = (time_int - initial_time)

        totalVals = np.hstack((storageVals, time_elapsed))

    return totalVals

def plot_data(totalVals, type):
    if type == "turbostat":
        xVal = 2
        yVal = 1
    elif type == "powerstat":
        xVal = 23
        yVal = 12
    else:
        xVal = 3
        yVal = 2

    plt.plot(totalVals[:,xVal], np.asfarray(totalVals[:,yVal]))
    firstSleep = totalVals[totalVals[:, xVal] < 10]
    plt.plot(firstSleep[:, xVal], firstSleep[:,yVal], c = 'b', label = "Sleep for 10 sec", linewidth = 4)

    condition1 = totalVals[:, xVal] >= 10 
    condition2 = totalVals[:, xVal] <= 11
    combined_condition1 = condition1 & condition2
    writeFirst = totalVals[combined_condition1]
    plt.plot(writeFirst[:, xVal], writeFirst[:,yVal], c = 'g', label = "Write 1 to 9", linewidth = 4)


    condition3 = totalVals[:, xVal] >= 11 
    condition4 = totalVals[:, xVal] <= 14
    combined_condition2 = condition3 & condition4
    write10First = totalVals[combined_condition2]
    plt.plot(write10First[:, xVal], write10First[:,yVal], c= 'r', label = "Write 10", linewidth = 4)


    condition5 = totalVals[:, xVal] >= 14
    condition6 = totalVals[:, xVal] <= 24
    combined_condition3 = condition5 & condition6
    secondSleep = totalVals[combined_condition3]
    plt.plot(secondSleep[:, xVal], secondSleep[:,yVal], c = 'b', linewidth = 4)

    condition7 = totalVals[:, xVal] >= 24 
    condition8 = totalVals[:, xVal] <= 86
    combined_condition4 = condition7 & condition8
    writeSecond = totalVals[combined_condition4]
    plt.scatter(totalVals[totalVals[:, xVal] == 24][:, xVal], totalVals[totalVals[:, xVal] == 24][:,yVal], c = 'g', linewidth = 4)
    # plt.plot(writeSecond[:, xVal], writeSecond[:,yVal], c = 'g', linewidth = 4)



    condition9 = totalVals[:, xVal] >= 24 
    condition10 = totalVals[:, xVal] <= 28
    combined_condition5 = condition9 & condition10
    write10Second = totalVals[combined_condition5]
    plt.plot(write10Second[:, xVal], write10Second[:,yVal], c = 'r', linewidth = 4)


    condition11 = totalVals[:, xVal] >= 28 
    conditiony12 = totalVals[:, xVal] <= 38
    combined_condition6 = condition11 & conditiony12
    thirdSleep = totalVals[combined_condition6]
    plt.plot(thirdSleep[:, xVal], thirdSleep[:,yVal], c = 'b', linewidth = 4)


    condition13 = totalVals[:, xVal] >= 150 
    condition14 = totalVals[:, xVal] <= 158
    combined_condition7 = condition13 & condition14
    writeThird = totalVals[combined_condition7]
    plt.scatter(totalVals[totalVals[:, xVal] == 38][:, xVal], totalVals[totalVals[:, xVal] == 38][:,yVal], c = 'g', linewidth = 4)
    #plt.plot(writeThird[:, xVal], writeThird[:, yVal], c = 'g', linewidth = 4)

    condition15 = totalVals[:, xVal] >= 38 
    condition16 = totalVals[:, xVal] <= 41
    combined_condition8 = condition15 & condition16
    write10Third = totalVals[combined_condition8]
    plt.plot(write10Third[:, xVal], write10Third[:,yVal], c = 'r', linewidth = 4)

    plt.plot(totalVals[totalVals[:,xVal] > 41][:,xVal], totalVals[totalVals[:,xVal] > 41][:, yVal], linewidth = 4, label = "Program Finished")
    plt.legend()
    plt.xlabel("Time Elapsed (seconds)")
    plt.ylabel("RAM Power Usage (Watts)")
    plt.xticks(range(0,75,5))
    plt.yticks(range(0,150,10))
    plt.title("RAM Power Report Read (Disk)")

    plt.show()


if __name__ == "__main__": #will not execute test function when the file is imported
    clean = prep_data(sys.argv[1], sys.argv[2])
    plot_data(clean, sys.argv[2])



