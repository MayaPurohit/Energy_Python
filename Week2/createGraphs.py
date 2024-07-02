import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.linalg import lstsq

super_simple = pd.read_csv("/Data/receive_times.csv").to_numpy()

# sizes = super_simple[:, 4] * 10
# colors = super_simple[:, 4] 

plt.plot(super_simple[:, 0], super_simple[:,12])
# plt.scatter(super_simple[:, 0], super_simple[:,12])
plt.xlabel("Time Elapsed (seconds)")
plt.ylabel("CPU Power Usage (Watts)")
plt.xticks(range(0,130,10))
plt.yticks(range(0,130,10))
plt.title("CPU Power Usage")

plt.show()



# plt.plot(super_simple[:, 0], super_simple[:, 2])
# plt.xlabel("Time Elapsed (seconds)")
# plt.ylabel("Watts")
# plt.title("Watts used by DRAM")
# plt.xticks(range(0, 85, 5))
# plt.yticks(range(0, 14, 1))
# plt.show()


#develop arrays for linear regression
# section = super_simple[super_simple[:, 5] != 0, :]
# print(super_simple[super_simple[:, 5] != 0, :])
# A = np.array(section[:, 5], dtype = float)
# A = np.reshape(A, (A.shape[0], 1))
# intercepts = np.ones((A.shape[0], 1))
# A1 = np.hstack([intercepts, A])
# y = np.array(section[:, 12], dtype = float)
# y = np.reshape(y, (y.shape[0], 1))
# c, res, _, _, = lstsq(A1, y) #finds the slope and the intercepts 
# slope = np.reshape(c[1:], (c[1:].shape[0], 1))
# intercept = c[0,0]



# #get R^2 value
# mean = np.mean(y)
# S = np.sum((y - mean)**2)
# R2 = 1 - (res/S)

# #plot the points and the regression line 
# x = np.linspace(0, 2)
# y = intercept+ slope[0]*x
# plt.plot(x,y, 'r', label = "Regression Line")
# plt.scatter(section[:, 5], section[:, 12])
# plt.xlabel("Percentage of Task Waiting for IO Operation")
# plt.ylabel("Watts")
# plt.title("Watts vs. IO Wait Time: R^2 = %.2f" % R2)
# plt.xticks(np.linspace(0, 2, 9))
# plt.yticks(range(0, 130, 10))
# plt.show()