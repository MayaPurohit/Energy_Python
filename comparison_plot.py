import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
import pandas as pd
import plot_data
# from scipy.linalg import lstsq


# disk = plot_data.prep_data(r"C:\Users\mayam\OneDrive\Desktop\BigDataX\Week5\Disk\turbostat\turbostat_disk_read.csv", "turbostat", "client", False)
# memory = plot_data.prep_data(r"C:\Users\mayam\OneDrive\Desktop\BigDataX\Week5\Memory\turbostat\turbostat_memory_read.csv", "turbostat", "client", False)
# lustre = plot_data.prep_data(r"C:\Users\mayam\OneDrive\Desktop\BigDataX\Week5\Lustre Client Node\turbostat\turbostat_client_read.csv", "turbostat", "client", False)


def compare_plot(nodes, type, iotype, idle_consideration = False):
    for node in nodes:
        if type == "turbostat":
                xVal = 2
                yVal = 1
        elif type == "powerstat":
                if node == "nvme1" or  node == "nvme2":
                        xVal = 21
                elif node == "admin":
                        xVal = 26
                else:
                        xVal = 23
                yVal = 12
        else:
                xVal = 3
                yVal = 2

        filename = type + "_" + node + "_" + iotype +".csv"
        prepped = plot_data.prep_data(fr"C:\Users\mayam\OneDrive\Desktop\BigDataX\Week5\{node}\{type}\{filename}", type, node, idle_consideration)
        plt.plot(prepped[:, xVal], prepped[:, yVal], label = f"{node.capitalize()} Measurements") 
    
    plt.title(f"{nodes[0].capitalize()} vs. {nodes[1].capitalize()} vs. {nodes[2].capitalize()} ({type.upper()} Power Read)")
    plt.ylabel("Energy Power (Watts)")
    plt.xlabel("Time Elasped (seconds)")
    plt.legend()  
    plt.locator_params(axis='both', nbins=8)     
    plt.show()


compare_plot(["disk", "memory", "client"], "powerstat", "write", False)