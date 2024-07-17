import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
import pandas as pd
# from scipy.linalg import lstsq

clientVals8 = pd.read_csv("ipmi_interval_client_8.csv").to_numpy()
metadataVals8 = pd.read_csv("ipmi__interval_metadata-server_8.csv").to_numpy()
storageVals8 = pd.read_csv("ipmi__interval_storage_8.csv").to_numpy()

clientVals9 = pd.read_csv("ipmi_interval_client_9.csv").to_numpy()
metadataVals9 = pd.read_csv("ipmi__interval_metadata-server_9.csv").to_numpy()
storageVals9 = pd.read_csv("ipmi__interval_storage_9.csv").to_numpy()

clientVals10 = pd.read_csv("ipmi_interval_client_10.csv").to_numpy()
metadataVals10 = pd.read_csv("ipmi__interval_metadata-server_10.csv").to_numpy()
storageVals10 = pd.read_csv("ipmi__interval_storage_10.csv").to_numpy()

clientVals8 = clientVals8[clientVals8[:,2] >= 230]
metadataVals8 = metadataVals8[metadataVals8[:,2] >= 210]
storageVals8 = storageVals8[storageVals8[:,2] >= 130]


clientVals9 = clientVals9[clientVals9[:,2] >= 230]
metadataVals9 = metadataVals9[metadataVals9[:,2] >= 210]
storageVals9 = storageVals9[storageVals9[:,2] >= 130]

clientVals10 = clientVals10[clientVals10[:,2] >= 230]
metadataVals10 = metadataVals10[metadataVals10[:,2] >= 210]
storageVals10 = storageVals10[storageVals10[:,2] >= 130]

barWidth = 0.25
fig = plt.subplots(figsize =(8, 5)) 
print(clientVals10.shape[0])

eight = [clientVals8.shape[0],metadataVals8.shape[0], storageVals8.shape[0]]
print(eight)
nine = [clientVals9.shape[0], metadataVals8.shape[0], storageVals9.shape[0]]
print(nine)
ten = [clientVals10.shape[0], metadataVals10.shape[0], storageVals10.shape[0]]
print(ten)

br1 = np.arange(3) 
br2 = [x + barWidth for x in br1] 
br3 = [x + barWidth for x in br2] 


plt.bar(br1, eight, color ='r', width = barWidth, 
        edgecolor ='grey', label ='10^8') 
plt.bar(br2, nine, color ='g', width = barWidth, 
        edgecolor ='grey', label ='10^9') 
plt.bar(br3, ten, color ='b', width = barWidth, 
        edgecolor ='grey', label ='10^10') 

plt.xlabel("Nodes of the Lustre File System")
plt.ylabel("Number of Seconds of Time Spent")
plt.title("Duration of Time Spent Above Threshold Energy")
plt.xticks([r + barWidth for r in range(len(eight))],
        ['Client (230 Watts)', 'Metadata Server (210 Watts)', 'Storage Node (130 Watts)'])

plt.legend()

plt.show()



 