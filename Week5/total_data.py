import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
import pandas as pd
# from scipy.linalg import lstsq


ipmi = pd.read_csv("ipmi_memory_read_clean.csv").to_numpy()
powerstat = pd.read_csv("powerstat_memory_read_clean.csv").to_numpy()
turbostat = pd.read_csv("turbostat_memory_read_clean.csv").to_numpy()


powerstat = powerstat[powerstat[:,24] <=48]
turbostat = turbostat[turbostat[:,3] <=48]
# ipmi = ipmi[ipmi[:,4] <=38]


print(ipmi)
print(turbostat)
print(powerstat)

sum = turbostat[:,2] + powerstat[:,13]
print(sum)

plt.plot(powerstat[:, 24], powerstat[:, 13], label = "CPU Measurements")
plt.plot(turbostat[:,3], turbostat[:,2], label = "RAM Measurements")
plt.plot(ipmi[:, 4], ipmi[:, 3], label = "Total Power Consumption")
plt.plot(turbostat[:,3], sum, label = "CPU + RAM")
plt.legend(loc = "center right")
plt.title("Memory Read Power Analysis")
plt.ylabel("Energy Power (Watts)")
plt.xlabel("Time Elasped (seconds)")
plt.xticks(range(0,55,5))
plt.yticks(range(0,300,20))
plt.show()