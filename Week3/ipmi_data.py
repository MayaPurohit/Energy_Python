import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
# from scipy.linalg import lstsq

super_simple = pd.read_csv("ipmi_logCh.csv").to_numpy()

# subsetCurrent = super_simple[super_simple[:, 2] == "Current"]
# subsetMin = super_simple[super_simple[:, 2] == "Minimum"]
# subsetMax = super_simple[super_simple[:, 2] == "Maximum"]
# subsetAverage = super_simple[super_simple[:, 2] == "Average"]
plt.plot(super_simple[:, 0], super_simple[:,3], label = "Total")
plt.plot(super_simple[:, 0], super_simple[:,4], label = "CPU")
plt.plot(super_simple[:, 0], super_simple[:,5], label = "Difference")
# plt.plot(subsetAverage[:, 0], subsetAverage[:,3], label = "Average")

# plt.scatter(super_simple[:, 0], super_simple[:,12])
plt.xlabel("Time Elapsed (seconds)")
plt.ylabel("IPMI Power Value (Watts)")
plt.xticks(range(0,110,10))
plt.yticks(range(0,300,30))
plt.legend(loc = "upper right")
plt.title("IPMI Power Report")

plt.show()