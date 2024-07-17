import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
# from scipy.linalg import lstsq

super_simple = pd.read_csv("ipmi_current_read.csv").to_numpy()

# subsetCurrent = super_simple[super_simple[:, 2] == "Current"]
# print(subsetCurrent)
# DF = pd.DataFrame(subsetCurrent) 
# DF.to_csv("ipmi_current_read.csv")

plt.plot(super_simple[:, 0], super_simple[:,1], label = "Total")
plt.plot(super_simple[:, 0], super_simple[:,2], label = "CPU")
plt.plot(super_simple[:, 0], super_simple[:,3], label = "Difference")
plt.xlabel("Time Elapsed (seconds)")
plt.ylabel("IPMI Power Value (Watts)")
plt.xticks(range(0,120,20))
plt.yticks(range(0,200,35))
plt.legend(loc = "upper right")
plt.title("IPMI Power Report")





# subsetMin = super_simple[super_simple[:, 2] == "Minimum"]
# subsetMax = super_simple[super_simple[:, 2] == "Maximum"]
# subsetAverage = super_simple[super_simple[:, 2] == "Average"]
# plt.plot(subsetCurrent[:, 0], subsetCurrent[:,3], label = "Current")
# plt.plot(subsetMax[:, 0], subsetMax[:,3], label = "Maximum")
# plt.plot(subsetMin[:, 0], subsetMin[:,3], label = "Maximum")
# plt.plot(subsetAverage[:, 0], subsetAverage[:,3], label = "Average")
# plt.xlabel("Time Elapsed (seconds)")
# plt.ylabel("IPMI Power Value (Watts)")
# plt.xticks(range(0,120,20))
# plt.yticks(range(0,550,50))
# plt.legend(loc = "center right")
# plt.title("IPMI Power Report")


# # plt.scatter(super_simple[:, 0], super_simple[:,12])
# plt.xlabel("Time Elapsed (seconds)")
# plt.ylabel("IPMI Power Value (Watts)")
# plt.xticks(range(0,120,20))
# plt.yticks(range(0,550,50))
# plt.legend(loc = "center right")
# plt.title("IPMI Power Report")

plt.show()