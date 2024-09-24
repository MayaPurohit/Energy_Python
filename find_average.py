import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
import pandas as pd
import sys
# from scipy.linalg import lstsq
import plot_data


average1 = plot_data.prep_data(r"C:\Users\mayam\OneDrive\Desktop\BigDataX\AllAreas.csv", "powerstat", "write")
# average2 = plot_data.prep_data(r"C:\Users\mayam\OneDrive\Desktop\BigDataX\Week5\client\powerstat\powerstat_client_102.csv", "powerstat")
# average3 = plot_data.prep_data(r"C:\Users\mayam\OneDrive\Desktop\BigDataX\Week5\client\powerstat\powerstat_client_103.csv", "powerstat")


print(average1)
print(np.mean(average1[:, 12]))
# print(np.mean(average2[:, 12]))
# print(np.mean(average3[:, 12]))

# print((np.mean(average1[:, 12])+ np.mean(average2[:, 12])+ np.mean(average3[:, 12])) / 3)