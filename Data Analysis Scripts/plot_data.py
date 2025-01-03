import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
import pandas as pd
import sys
# from scipy.linalg import lstsq

idleMeasurements =  pd.read_csv(fr"C:\Users\mayam\Energy_Python\Data Analysis Scripts\idle_measurements.csv").to_numpy()
# writeMeasurements = pd.read_csv("CPUWrite.csv").to_numpy()
# nowriteMeasurements = pd.read_csv("NoWriteMeasurements.csv").to_numpy()
# nowriteCPU = pd.read_csv("CPUNoWrite.csv").to_numpy()
# print(nowriteCPU)


IDXClient = 1
IDXMetadata = 2
IDXStorage = 3
IDXAdmin = 4
IDXNvme1 = 5
IDXNvme2 = 6

IDXIPMIIdle = 0
IDXCPUIdle = 1
IDXRAMIdle = 2

IDXIPMIWrite = 3
IDXCPUWrite= 4
IDXRAMWrite= 5

def prep_data(filename, typePower, iotype, typeNode = None, account_idle = False):
    if typePower == "turbostat":
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
        if account_idle == True:
            if typeNode == "client" or typeNode == "disk" or typeNode == "memory" or typeNode == "transferdisk" or typeNode == "transfermemory":
                totalVals[:,1] = totalVals[:,1] - idleMeasurements[IDXRAMIdle, IDXClient]
            elif typeNode == "metadata":
                totalVals[:,1] = totalVals[:,1] - idleMeasurements[IDXRAMIdle, IDXMetadata]
            elif typeNode == "storage":
                totalVals[:,1] = totalVals[:,1] - idleMeasurements[IDXRAMIdle, IDXStorage]
            elif typeNode == "admin" or typeNode == "diskadmin" or typeNode == "memoryadmin" or typeNode == "transferadmin":
                totalVals[:,1] = totalVals[:,1] - idleMeasurements[IDXRAMIdle, IDXAdmin]
            elif typeNode == "nvme1":
                totalVals[:,1] = totalVals[:,1] - idleMeasurements[IDXRAMIdle, IDXNvme1]
            else: 
                totalVals[:,1] = totalVals[:,1] - idleMeasurements[IDXRAMIdle, IDXNvme2]
            

            totalVals[:, 1][totalVals[:, 1] < 0] = 0


    elif typePower == "powerstat":
        storageVals = pd.read_csv(filename, delimiter =r'\s+').to_numpy()

        storageVals = storageVals[storageVals[:,0] != "Time"]
        storageVals[:,0] = "2024-07-06 " + storageVals[:, 0] 

        time_format = '%Y-%m-%d %H:%M:%S'

        time_elapsed = np.zeros([storageVals.shape[0], 1])
        initial_time = datetime.strptime(storageVals[0,0], time_format)
        initial_time = int(initial_time.timestamp())

        for i in range(storageVals.shape[0]):
            timeNum = datetime.strptime(storageVals[i,0], time_format)
            time_int = int(timeNum.timestamp())
            time_elapsed[i] = (time_int - initial_time)

        totalVals = np.hstack((storageVals, time_elapsed))
        totalVals[:, 12] = np.asfarray(totalVals[:,12])

        if account_idle == True:
            if typeNode == "client" or typeNode == "disk" or typeNode == "memory" or typeNode == "transferdisk" or typeNode == "transfermemory":
                totalVals[:,12] = totalVals[:,12] - idleMeasurements[IDXCPUIdle, IDXClient]
            elif typeNode == "metadata":
                totalVals[:,12] = totalVals[:,12] - idleMeasurements[IDXCPUIdle, IDXMetadata]
            elif typeNode == "storage":
                totalVals[:,12] = totalVals[:,12] - idleMeasurements[IDXCPUIdle, IDXStorage]
            elif typeNode == "admin" or typeNode == "diskadmin" or typeNode == "memoryadmin" or typeNode == "transferadmin":
                totalVals[:,12] = totalVals[:,12] - idleMeasurements[IDXCPUIdle, IDXAdmin]
            elif typeNode == "nvme1":
                totalVals[:,12] = totalVals[:,12] - idleMeasurements[IDXCPUIdle, IDXNvme1]
            else: 
                totalVals[:,12] = totalVals[:,12] - idleMeasurements[IDXCPUIdle, IDXNvme2]
            
            totalVals[:, 12][totalVals[:, 12] < 0] = 0
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

        # if iotype == "read":
        #     if typeNode == "nvme1":
        #         totalVals[:,2] = totalVals[:,2] - 200
        # #     # print(totalVals[:, 2])

        # if account_idle == True:
        #     if typeNode == "client" or typeNode == "disk" or typeNode == "memory" or typeNode == "transferdisk" or typeNode == "transfermemory":
        #         print(totalVals[:,2])
        #         totalVals[:,2] = totalVals[:,2] - idleMeasurements[IDXIPMIIdle, IDXClient]
        #         print(totalVals[:,2])
        #     elif typeNode == "metadata":
        #         totalVals[:,2] = totalVals[:,2] - idleMeasurements[IDXIPMIIdle, IDXMetadata]
        #     elif typeNode == "storage":
        #         totalVals[:,2] = totalVals[:,2] - idleMeasurements[IDXIPMIIdle, IDXStorage]
        #     elif typeNode == "admin" or typeNode == "diskadmin" or typeNode == "memoryadmin" or typeNode == "transferadmin":
        #         totalVals[:,2] = totalVals[:,2] - idleMeasurements[IDXIPMIIdle, IDXAdmin]
        #     elif typeNode == "nvme1":
        #         totalVals[:,2] = totalVals[:,2] - idleMeasurements[IDXIPMIIdle, IDXNvme1] 
        #     else: 
        #         totalVals[:,2] = totalVals[:,2] - idleMeasurements[IDXIPMIIdle, IDXNvme2] 
            
        #     totalVals[:, 2][totalVals[:, 2] < 0] = 0

        # print(idleMeasurements[IDXIPMIIdle, IDXClient])
    return totalVals

def removeCPU(filename, iotype, typeNode, size, considered):

    if iotype == "write":
        if size == 10:
            row = 0
        elif size == 9:
            row = 1
        else:
            row = 2
    else: 
        if size == 10:
            row = 3
        elif size == 9:
            row = 4
        else:
            row = 5

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

    # if typeNode == "nvme1":
    #     totalVals[:,2] = totalVals[:,2] - 200
    #     # print(totalVals[:, 2])

    if considered == True:
        if typeNode == "client":
            totalVals[:,2] = totalVals[:,2] - (nowriteMeasurements[row, 3] + nowriteCPU[row, 3])
        elif typeNode == "disk":
            totalVals[:,2] = totalVals[:,2] - (nowriteMeasurements[row, 1] + nowriteCPU[row, 1])
        elif typeNode == "memory":
            totalVals[:,2] = totalVals[:,2] - (nowriteMeasurements[row, 2] + nowriteCPU[row, 2])
        elif typeNode == "metadata":
            totalVals[:,2] = totalVals[:,2] - (nowriteMeasurements[row, 5] + nowriteCPU[row, 5])
        elif typeNode == "storage":
            totalVals[:,2] = totalVals[:,2] - (nowriteMeasurements[row, 4] + nowriteCPU[row, 4])
        elif typeNode == "admin": 
            totalVals[:,2] = totalVals[:,2] - (nowriteMeasurements[row, 8] + nowriteCPU[row, 8])
        elif typeNode == "diskadmin":
            totalVals[:,2] = totalVals[:,2] - (nowriteMeasurements[row, 7] + nowriteCPU[row, 7])
        elif typeNode == "memoryadmin":
            totalVals[:,2] = totalVals[:,2] - (nowriteMeasurements[row, 6] + nowriteCPU[row, 6])
        elif typeNode == "nvme1":
            print(totalVals[:,2])
            totalVals[:,2] = totalVals[:,2] - (nowriteMeasurements[row, 9] + nowriteCPU[row, 9])
            print(totalVals[:,2])
        else: 
            print(nowriteMeasurements[row, 10])
            print(totalVals[:,2])
            totalVals[:,2] = totalVals[:,2] - (nowriteMeasurements[row, 10] + nowriteCPU[row, 10])
            print(totalVals[:,2])

    
    totalVals[:, 2][totalVals[:, 2] < 0] = 0
    return totalVals

# def plot_data(totalVals, type):
#     if type == "turbostat":
#         xVal = 2
#         yVal = 1
#     elif type == "powerstat":
#         xVal = 23
#         yVal = 12
#     else:
#         xVal = 3
#         yVal = 2

#     plt.plot(totalVals[:,xVal], np.asfarray(totalVals[:,yVal]))
#     firstSleep = totalVals[totalVals[:, xVal] < 10]
#     plt.plot(firstSleep[:, xVal], firstSleep[:,yVal], c = 'b', label = "Sleep for 10 sec", linewidth = 4)

#     condition1 = totalVals[:, xVal] >= 10 
#     condition2 = totalVals[:, xVal] <= 11
#     combined_condition1 = condition1 & condition2
#     writeFirst = totalVals[combined_condition1]
#     plt.plot(writeFirst[:, xVal], writeFirst[:,yVal], c = 'g', label = "Write 1 to 9", linewidth = 4)


#     condition3 = totalVals[:, xVal] >= 11 
#     condition4 = totalVals[:, xVal] <= 14
#     combined_condition2 = condition3 & condition4
#     write10First = totalVals[combined_condition2]
#     plt.plot(write10First[:, xVal], write10First[:,yVal], c= 'r', label = "Write 10", linewidth = 4)


#     condition5 = totalVals[:, xVal] >= 14
#     condition6 = totalVals[:, xVal] <= 24
#     combined_condition3 = condition5 & condition6
#     secondSleep = totalVals[combined_condition3]
#     plt.plot(secondSleep[:, xVal], secondSleep[:,yVal], c = 'b', linewidth = 4)

#     condition7 = totalVals[:, xVal] >= 24 
#     condition8 = totalVals[:, xVal] <= 86
#     combined_condition4 = condition7 & condition8
#     writeSecond = totalVals[combined_condition4]
#     plt.scatter(totalVals[totalVals[:, xVal] == 24][:, xVal], totalVals[totalVals[:, xVal] == 24][:,yVal], c = 'g', linewidth = 4)
#     # plt.plot(writeSecond[:, xVal], writeSecond[:,yVal], c = 'g', linewidth = 4)



#     condition9 = totalVals[:, xVal] >= 24 
#     condition10 = totalVals[:, xVal] <= 28
#     combined_condition5 = condition9 & condition10
#     write10Second = totalVals[combined_condition5]
#     plt.plot(write10Second[:, xVal], write10Second[:,yVal], c = 'r', linewidth = 4)


#     condition11 = totalVals[:, xVal] >= 28 
#     conditiony12 = totalVals[:, xVal] <= 38
#     combined_condition6 = condition11 & conditiony12
#     thirdSleep = totalVals[combined_condition6]
#     plt.plot(thirdSleep[:, xVal], thirdSleep[:,yVal], c = 'b', linewidth = 4)


#     condition13 = totalVals[:, xVal] >= 150 
#     condition14 = totalVals[:, xVal] <= 158
#     combined_condition7 = condition13 & condition14
#     writeThird = totalVals[combined_condition7]
#     plt.scatter(totalVals[totalVals[:, xVal] == 38][:, xVal], totalVals[totalVals[:, xVal] == 38][:,yVal], c = 'g', linewidth = 4)
#     #plt.plot(writeThird[:, xVal], writeThird[:, yVal], c = 'g', linewidth = 4)

#     condition15 = totalVals[:, xVal] >= 38 
#     condition16 = totalVals[:, xVal] <= 41
#     combined_condition8 = condition15 & condition16
#     write10Third = totalVals[combined_condition8]
#     plt.plot(write10Third[:, xVal], write10Third[:,yVal], c = 'r', linewidth = 4)

#     plt.plot(totalVals[totalVals[:,xVal] > 41][:,xVal], totalVals[totalVals[:,xVal] > 41][:, yVal], linewidth = 4, label = "Program Finished")
#     plt.legend()
#     plt.xlabel("Time Elapsed (seconds)")
#     plt.ylabel("RAM Power Usage (Watts)")
#     plt.xticks(range(0,75,5))
#     plt.yticks(range(0,150,10))
#     plt.title("RAM Power Report Read (Disk)")

#     plt.show()




# if __name__ == "__main__": #will not execute test function when the file is imported
#     clean = prep_data(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
#     plot_data(clean, sys.argv[2])



