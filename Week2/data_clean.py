import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.linalg import lstsq

read = pd.read_csv("Week2Data/turbostatVals_writeClean.csv").to_numpy()
read = read[read[:, 0] %3 == 0]
print(read)
df = pd.DataFrame(read)
df.to_csv("Week2Data/turbostatVals_write.csv")