import scipy.integrate
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
import pandas as pd
import plot_data
from scipy.linalg import lstsq

import seaborn as sns

powers = ["ipmi"]
machines = ["diskadmin", "memoryadmin", "admin", "nvme1", "nvme2"]
finalDict = {}
plt.rcParams.update({'font.size': 13})


def generate_area(types, nodes, iotype, idle_considered = False):
        j = -1
        # dataset = np.zeros((6,3,1))
        finalDict = {}
        for type in types:
                for node in nodes:
                        j += 1
                        if type == "turbostat":
                                xVal = 2
                                yVal = 1
                        elif type == "powerstat":
                                if node == "nvme1" or  node == "nvme2":
                                        xVal = 21
                                elif node == "admin" or node == "diskadmin" or node == "memoryadmin":
                                        xVal = 26
                                else:
                                        xVal = 23
                                yVal = 12
                        else:
                                xVal = 3
                                yVal = 2
                        threeVals = np.zeros((3,))
                        for i in range(1,4):
                                if i == 1:
                                        filename = type + "_" + node + "_" + iotype + ".csv"
                                else:
                                        filename = type + "_" +  node + "_" + iotype + str(i) + ".csv"
                                print(filename)
                                val = plot_data.prep_data(fr"C:\Users\mayam\OneDrive\Desktop\BigDataX\Week5\{node}\{type}\{filename}", type, iotype, node, idle_considered)
                                area = scipy.integrate.simpson(val[:, yVal], x = val[:, xVal])
                                # print(filename + ": " + str(val.shape[0]) + " " + str(area))
                                threeVals[i-1] = area
                                # print(node + ": ", threeVals)
                        
                        # dataset[j] = np.reshape(threeVals, (3, 1))
                        # print(node + ": " + str(threeVals))
                        average = np.mean(threeVals)
                        # print(node + "_" + type, threeVals)
                        std = np.std(threeVals)
                        finalDict[type + "_" + node] = [average, std]
        # print(dataset)
        # dataset = np.reshape(dataset, (18,1))
        # data = pd.DataFrame(dataset)
        # data.to_csv("Turboareas.csv", index = False, index_label= False)
        return finalDict

# idle = True
finalDict = generate_area(powers, machines, "write", True)
print(finalDict)
finalDictRead = generate_area(powers, machines, "read", True)
print(finalDictRead)




dictKeys = list(finalDict.keys())
dictKeysRead = list(finalDictRead.keys())


# node1 = np.array([finalDict[dictKeys[0]][0], finalDict[dictKeys[len(machines)]][0], finalDict[dictKeys[2*len(machines)]][0]])
# node2 = np.array([finalDict[dictKeys[1]][0], finalDict[dictKeys[len(machines) + 1]][0], finalDict[dictKeys[2*len(machines) + 1]][0]])
# node3 = np.array([finalDict[dictKeys[2]][0], finalDict[dictKeys[len(machines) + 2]][0], finalDict[dictKeys[2*len(machines) + 2]][0]])
# node4 = np.array([finalDict[dictKeys[3]][0], finalDict[dictKeys[len(machines) + 3]][0], finalDict[dictKeys[2*len(machines) + 3]][0]])
# node5 = np.array([finalDict[dictKeys[4]][0], finalDict[dictKeys[len(machines) +4]][0], finalDict[dictKeys[2*len(machines) + 4]][0]])


# node1 = np.array([finalDict[dictKeys[0]][0], finalDict[dictKeys[len(machines)]][0], turbostatAdmin["turbostat_diskadmin"][0]])
# node2 = np.array([finalDict[dictKeys[1]][0], finalDict[dictKeys[len(machines) + 1]][0], turbostatAdmin["turbostat_memoryadmin"][0]])
# node3 = np.array([finalDict[dictKeys[2]][0], finalDict[dictKeys[len(machines) + 2]][0], turbostatAdmin["turbostat_admin"][0]])
# node4 = np.array([finalDict[dictKeys[3]][0], finalDict[dictKeys[len(machines) + 3]][0], 0])
# node5 = np.array([finalDict[dictKeys[4]][0], finalDict[dictKeys[len(machines) +4]][0], 0])


# node1 = np.array([finalDict[dictKeys[0]][0], finalDictRead[dictKeysRead[0]][0]])
# node2 = np.array([finalDict[dictKeys[1]][0], finalDictRead[dictKeysRead[1]][0]])
# node3 = np.array([finalDict[dictKeys[2]][0], finalDictRead[dictKeysRead[2]][0]])
# node4 = np.array([finalDict[dictKeys[3]][0], finalDictRead[dictKeysRead[3]][0]])
# node5 = np.array([finalDict[dictKeys[4]][0], finalDictRead[dictKeysRead[4]][0]])


# err1 = np.array([finalDict[dictKeys[0]][1], finalDict[dictKeys[len(machines)]][1], finalDict[dictKeys[2*len(machines)]][1]])
# err2 = np.array([finalDict[dictKeys[1]][1], finalDict[dictKeys[len(machines) + 1]][1], finalDict[dictKeys[2*len(machines) + 1]][1]])
# err3 = np.array([finalDict[dictKeys[2]][1], finalDict[dictKeys[len(machines) + 2]][1], finalDict[dictKeys[2*len(machines) + 2]][1]])
# err4 = np.array([finalDict[dictKeys[3]][1], finalDict[dictKeys[len(machines) + 3]][1], finalDict[dictKeys[2*len(machines) + 3]][1]])
# err5 = np.array([finalDict[dictKeys[3]][1], finalDict[dictKeys[len(machines) + 4]][1], finalDict[dictKeys[2*len(machines) + 4]][1]])


# err1 = np.array([finalDict[dictKeys[0]][1], finalDict[dictKeys[len(machines)]][1], turbostatAdmin["turbostat_diskadmin"][1]])
# err2 = np.array([finalDict[dictKeys[1]][1], finalDict[dictKeys[len(machines) + 1]][1], turbostatAdmin["turbostat_memoryadmin"][1]])
# err3 = np.array([finalDict[dictKeys[2]][1], finalDict[dictKeys[len(machines) + 2]][1], turbostatAdmin["turbostat_admin"][1]])
# err4 = np.array([finalDict[dictKeys[3]][1], finalDict[dictKeys[len(machines) + 3]][1], 0])
# err5 = np.array([finalDict[dictKeys[3]][1], finalDict[dictKeys[len(machines) + 4]][1], 0])

# err1 = np.array([finalDict[dictKeys[0]][1], finalDictRead[dictKeysRead[0]][1]])
# err2 = np.array([finalDict[dictKeys[1]][1], finalDictRead[dictKeysRead[1]][1]])
# err3 = np.array([finalDict[dictKeys[2]][1], finalDictRead[dictKeysRead[2]][1]])
# err4 = np.array([finalDict[dictKeys[3]][1], finalDictRead[dictKeysRead[3]][1]])
# err5 = np.array([finalDict[dictKeys[4]][1], finalDictRead[dictKeysRead[4]][1]])

# fig = plt.subplots(figsize =(8, 5)) 
# barWidth = 0.2

# br1 = np.arange(2) 
# br2 = [x + barWidth for x in br1] 
# br3 = [x + barWidth for x in br2] 
# # br4 = [x + barWidth for x in br3] 
# categories = ["Write", "Read"]
# print(br1)

# plt.bar(br1, node1, yerr = err1, color ='#ff9999', width = barWidth, 
#         edgecolor ='grey', label = "Disk")
# plt.bar(br2, node2, yerr = err2, color ='lightgreen', width = barWidth, 
#         edgecolor ='grey', label = "Memory") 
# plt.bar(br3, height = node3, yerr = err3, color ='lightblue', width = barWidth, 
#         edgecolor ='grey', label = "DAOS Client") 
# plt.bar(br3, node4, bottom = node3, yerr = err4, color ='#CBC3E3', width = barWidth, 
#         edgecolor ='grey', label = "NVMe 1") 
# plt.bar(br3, node5, bottom = node3 + node4, yerr = err5, color ="bisque", width = barWidth, 
#         edgecolor ='grey', label = "NVMe 2") 

# plt.xlabel("Energy Metrics (Watts)")
# plt.ylabel("Total Energy (Joules)")
# # plt.title("Power Used Reading Idle Consideration (Disk vs Memory vs. Lustre Total)")
# plt.yticks(range(0, 14000, 1000))
# plt.xticks([r + barWidth for r in range(len(node1))],
#         categories)

# plt.legend()

# plt.show()


fig = plt.subplots(figsize =(9, 6)) 

# Lustre Figure
NVMESize = pd.read_csv("WriteLustreSize.csv").to_numpy()
NVMESize = NVMESize[NVMESize[:, 0] == "Client"]
print(NVMESize[:, 8])

intercepts = np.ones((NVMESize.shape[0],1))
A1 = np.hstack((intercepts, np.reshape(NVMESize[:, 8], (NVMESize[:, 8].shape[0], 1))))
A1 = np.array(A1, dtype = "float")

fullList = []
for val in NVMESize[:, 4]:
    fullList.append(float(val))
c1, res, _, _, = lstsq(A1,np.array(fullList)) #finds the slope and the intercepts 
print(c1)
xvals = np.linspace(np.min(NVMESize[:, 8]), np.max(NVMESize[:, 8]))

plt.scatter(NVMESize[:, 8], fullList)
plt.plot(xvals, c1[0] + c1[1]*xvals, label = "Lustre Client")

plt.annotate(r'$Actual Client = 24.58 + 12.43(Predicted Client)$', xy=(7.5, 200), xytext=(0, 550),
             arrowprops=dict(facecolor='black', shrink=0.05),
             fontsize=13)

storage = pd.read_csv("Storage.csv").to_numpy()


intercepts = np.ones((storage.shape[0],1))
A1 = np.hstack((intercepts, np.reshape(storage[:, 6], (storage[:, 6].shape[0], 1))))
A1 = np.array(A1, dtype = "float")

fullList = []
for val in storage[:, 2]:
    fullList.append(float(val))
c1, res, _, _, = lstsq(A1,np.array(fullList)) #finds the slope and the intercepts 
print(c1)
xvals = np.linspace(np.min(storage[:, 6]), np.max(storage[:, 6]))
# print(xvals)
plt.scatter(storage[:, 6], fullList)
plt.plot(xvals, c1[0] + c1[1]*xvals, label = "Lustre Storage")


plt.annotate(r'$Actual Metadata = -18.18 + 2.37(Predicted Metadata)$', xy=(50, 150), xytext=(50, 450),
             arrowprops=dict(facecolor='black', shrink=0.05),
             fontsize=13)

metadata = pd.read_csv("LustreNodes.csv").to_numpy()


intercepts = np.ones((metadata.shape[0],1))
A1 = np.hstack((intercepts, np.reshape(metadata[:, 7], (metadata[:, 7].shape[0], 1))))
A1 = np.array(A1, dtype = "float")

fullList = []
for val in metadata[:, 3]:
    fullList.append(float(val))
c1, res, _, _, = lstsq(A1,np.array(fullList)) #finds the slope and the intercepts 
print(c1)
xvals = np.linspace(np.min(metadata[:, 7]), np.max(metadata[:, 7]))
# print(xvals)
plt.scatter(metadata[:, 7], fullList)
plt.plot(xvals, c1[0] + c1[1]*xvals, label = "Metadata Node")

plt.annotate(r'$Actual Storage = -5.07 + 0.79(Predicted Storage)$', xy=(20, 15), xytext=(75, 0),
             arrowprops=dict(facecolor='black', shrink=0.05),
             fontsize=13)


#DAOS Figure

# NVMESize = pd.read_csv("WriteDAOSSize.csv").to_numpy()
# NVMESize = NVMESize[NVMESize[:, 0] == "DAOS"]
# print(NVMESize[:, 8])

# intercepts = np.ones((NVMESize.shape[0],1))
# A1 = np.hstack((intercepts, np.reshape(NVMESize[:, 8], (NVMESize[:, 8].shape[0], 1))))
# A1 = np.array(A1, dtype = "float")

# fullList = []
# for val in NVMESize[:, 4]:
#     fullList.append(float(val))
# c1, res, _, _, = lstsq(A1,np.array(fullList)) #finds the slope and the intercepts 
# print(c1)
# xvals = np.linspace(np.min(NVMESize[:, 8]), np.max(NVMESize[:, 8]))

# plt.scatter(NVMESize[:, 8], fullList)
# plt.plot(xvals, c1[0] + c1[1]*xvals, label = "DAOS Client")

# plt.annotate(r'$Actual Client = 27.9 + 3.36(Predicted Client)$', xy=(7.5, 150), xytext=(0, 800),
#              arrowprops=dict(facecolor='black', shrink=0.05),
#              fontsize=13)

# storage = pd.read_csv("NVMe Storage.csv").to_numpy()


# intercepts = np.ones((storage.shape[0],1))
# A1 = np.hstack((intercepts, np.reshape(storage[:, 8], (storage[:, 8].shape[0], 1))))
# A1 = np.array(A1, dtype = "float")

# fullList = []
# for val in storage[:, 3]:
#     fullList.append(float(val))
# c1, res, _, _, = lstsq(A1,np.array(fullList)) #finds the slope and the intercepts 
# print(c1)
# xvals = np.linspace(np.min(storage[:, 8]), np.max(storage[:, 8]))
# # print(xvals)
# plt.scatter(storage[:, 8], fullList)
# plt.plot(xvals, c1[0] + c1[1]*xvals, label = "DAOS Metadata/Storage")


# plt.annotate(r'$Actual Storage = -82.1 + 3.43(Predicted Storage)$', xy=(75, 200), xytext=(100, 100),
#              arrowprops=dict(facecolor='black', shrink=0.05),
#              fontsize=13)





plt.xlabel("Predicted Energy from Model (J)")
plt.ylabel("Actual Energy (J)")
# plt.yticks(range(0,350,25))
plt.legend()
plt.show()