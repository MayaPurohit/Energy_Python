import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
import pandas as pd
import plot_data
# from scipy.linalg import lstsq


ipmi = plot_data.prep_data(r"C:\Users\mayam\OneDrive\Desktop\BigDataX\Week6\client\IPMI\ipmi_client_read.csv", "ipmi", "client", True)
powerstat = plot_data.prep_data(r"C:\Users\mayam\OneDrive\Desktop\BigDataX\Week5\client\Powerstat\powerstat_client_read.csv", "powerstat", "client", True)
turbostat = plot_data.prep_data(r"C:\Users\mayam\OneDrive\Desktop\BigDataX\Week5\client\Turbostat\turbostat_client_read.csv", "turbostat", "client", True)


ipmi = ipmi[ipmi[:,3] <=38]
# turbostat = turbostat[turbostat[:,2] <=332]
powerstat = powerstat[powerstat[:,23] <=38]



print(ipmi)
print(turbostat)
print(powerstat)

sum = turbostat[:,1] + powerstat[:,12]

plt.plot(powerstat[:, 23], powerstat[:, 12], label = "CPU Measurements")
plt.plot(turbostat[:,2], turbostat[:,1], label = "RAM Measurements")
plt.plot(ipmi[:, 3], ipmi[:, 2], label = "Total Power Consumption")
plt.plot(turbostat[:,2], sum, label = "CPU + RAM")
plt.legend(loc = "lower right")
plt.title("Client Power Analysis (Read)")
plt.ylabel("Energy Power (Watts)")
plt.xlabel("Time Elasped (seconds)")
plt.xticks(range(0,50,5))
plt.yticks(range(-70,70,10))
plt.show()


