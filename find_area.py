import scipy.integrate
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
import pandas as pd
import plot_data

def find_area(node, type, iotype, idle_considered = True):
    allAreas = []
    for i in range(1,4):
        if node == "lustre":
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
            mach = ["client", "metadata", "storage"]
            totalArea = 0
            for m in mach:
                if type == "turbostat":
                    xVal = 2
                    yVal = 1
                elif type == "powerstat":
                    if m == "nvme1" or  m == "nvme2":
                            xVal = 21
                    elif m == "admin" or m == "diskadmin" or m == "memoryadmin":
                            xVal = 26
                    else:
                            xVal = 23
                    yVal = 12
                else:
                    xVal = 3
                    yVal = 2
                if i == 1:
                    filename = type + "_" + m + "_"+iotype +".csv"
                else:
                    filename = type + "_" + m + "_" +iotype + str(i) +".csv"

                val = plot_data.prep_data(fr"C:\Users\mayam\OneDrive\Desktop\BigDataX\Week5\{m}\{type}\{filename}", type, iotype, m, idle_considered)
                area = scipy.integrate.simpson(val[:, yVal], x = val[:, xVal])
                totalArea += area 
            allAreas.append(totalArea)       
        elif node == "daos":
            mach = ["admin", "nvme1", "nvme2"]
            totalArea = 0
            for m in mach:
                print(m)
                if type == "turbostat":
                    xVal = 2
                    yVal = 1
                elif type == "powerstat":
                    if m == "nvme1" or  m == "nvme2":
                            xVal = 21
                    elif m == "admin" or m == "diskadmin" or m == "memoryadmin":
                            xVal = 26
                    else:
                            xVal = 23
                    yVal = 12
                else:
                    xVal = 3
                    yVal = 2
                if i == 1:
                    filename = type + "_" + m + "_"+iotype +".csv"
                else:
                    filename = type + "_" + m + "_" +iotype + str(i) +".csv"
                val = plot_data.prep_data(fr"C:\Users\mayam\OneDrive\Desktop\BigDataX\Week5\{m}\{type}\{filename}", type, iotype, m, idle_considered)
                area = scipy.integrate.simpson(val[:, yVal], x = val[:, xVal])

                totalArea += area
            allAreas.append(totalArea)  

        else:
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
            if i == 1:
                filename = type + "_" + node+ "_"+iotype +".csv"
            else:
                filename = type + "_" + node + "_" +iotype + str(i) +".csv"
            print(filename)
            val = plot_data.prep_data(fr"C:\Users\mayam\OneDrive\Desktop\BigDataX\Week5\{node}\{type}\{filename}", type, iotype, node, idle_considered)
            totalArea = scipy.integrate.simpson(val[:, yVal], x = val[:, xVal])
        
        allAreas.append(totalArea)  
        
    return allAreas


print(find_area("diskadmin", "ipmi", "read", idle_considered=True))

# def interval(node, iotype, power10, idle_considered = True):
#     xVal = 3
#     yVal = 2
#     allAreas = []
#     for i in range(1,4):
#         if node == "lustre":
#             mach = ["client", "metadata", "storage"]
#             totalArea = 0
#             for m in mach:
#                 if iotype == "read":
#                     filename =  "ipmi_" + m + "_" +iotype + str(power10)+ str(i) +".csv"
#                 else:
#                     filename =  "ipmi_" + m + "_" + str(power10)+ str(i) +".csv"   
#                 val = plot_data.removeCPU(fr"C:\Users\mayam\OneDrive\Desktop\BigDataX\Week5\{m}\ipmi\{filename}", iotype, m, power10, idle_considered)
#                 print(val)
#                 area = scipy.integrate.simpson(val[:, yVal], x = val[:, xVal], even = "first")
#                 print(filename+ ": " , val)
#                 totalArea += area 
#             allAreas.append(totalArea)       
#         elif node == "daos":
#             mach = ["admin", "nvme1", "nvme2"]
#             totalArea = 0
#             for m in mach:
#                 if iotype == "read":
#                     filename =  "ipmi_" + m + "_" +iotype + str(power10)+ str(i) +".csv"
#                 else:
#                     filename =  "ipmi_" + m + "_" + str(power10)+ str(i) +".csv"    
#                 val = plot_data.removeCPU(fr"C:\Users\mayam\OneDrive\Desktop\BigDataX\Week5\{m}\ipmi\{filename}",iotype, m, power10, idle_considered)

#                 area = scipy.integrate.simpson(val[:, yVal], x = val[:, xVal])

#                 totalArea += area
#             allAreas.append(totalArea)  

#         else:
#             if iotype == "read":
#                 filename =  "ipmi_" + node + "_" +iotype + str(power10)+ str(i) +".csv"
#             else:
#                 filename =  "ipmi_" + node + "_" + str(power10)+ str(i) +".csv"     
#             val = plot_data.removeCPU(fr"C:\Users\mayam\OneDrive\Desktop\BigDataX\Week5\{node}\ipmi\{filename}",iotype, node, power10, idle_considered)
#             print(filename)
#             totalArea = scipy.integrate.simpson(val[:, yVal], x = val[:, xVal])
        
#         allAreas.append(totalArea)  
        
#     return allAreas



# # print(interval("client", "write",10, True))
# val = plot_data.removeCPU(fr"C:\Users\mayam\OneDrive\Desktop\BigDataX\Week5\disk\ipmi\ipmi_memoryadmin_103.csv","write", "disk", 10, True)
# totalArea = scipy.integrate.simpson(val[:, 2], x = val[:, 3])
# print(totalArea)