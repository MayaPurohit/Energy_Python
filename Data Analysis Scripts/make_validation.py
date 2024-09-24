import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
import pandas as pd
import sys
# from scipy.linalg import lstsq


def make_validation_set(filename):
    trainSet = pd.read_csv(filename).to_numpy()[1:, :]
    valSet = trainSet[2::3]
    valSet = pd.DataFrame(valSet)
    valSet.to_csv("WriteLustreVal.csv", index = False, index_label= False)
    indices_to_remove = np.arange(2, trainSet.shape[0], 3)
    trainSet = np.delete(trainSet, indices_to_remove, axis=0)
    trainSet = pd.DataFrame(trainSet)
    trainSet.to_csv("WriteLustreTrain.csv", index = False, index_label= False)


make_validation_set(r"C:\Users\mayam\OneDrive\Desktop\CS251_Projects\Project3\data\WriteLustreSize.csv")
