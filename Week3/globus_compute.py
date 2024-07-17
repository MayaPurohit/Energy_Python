from globus_compute_sdk import Executor
from globus_compute_sdk import Client
from proxystore.connectors.endpoint import EndpointConnector
from proxystore.connectors.file import FileConnector
from proxystore.proxy import Proxy
from proxystore.proxy import resolve, is_resolved
from proxystore.store import Store
import os 


ENDPOINT_UUID = '43eaa6c7-589e-45f1-9194-ae45f5fa28c9'
ENDPOINT_CHAMELEON = "720771de-5a2c-4489-b8da-893353f9074b"

def monitor(p: Proxy):
    import os
    import subprocess
    import time

    # os.system("sudo powerstat -a -RDH 1 80 >globus_times.csv &")
    result = subprocess.run(["sudo powerstat -a -RDH 1 80 >globus_times.csv"], capture_output=True, text=True, check=True, shell = True)
    # time.sleep(10)
    return resolve(p)


#'c047182f-9d0b-4692-a012-5c228fc4fc6c'
store = Store('my-store', EndpointConnector(endpoints=['75dd4b0b-7b54-4cf3-a2b3-0f56a0fe8956', '06acf236-b860-4c89-b863-b2c68bac0315']), register=True)
#store = Store('my-store', FileConnector('./proxystore-cache'), register=True)  

with Executor(endpoint_id=ENDPOINT_CHAMELEON) as gce:
    file_val = os.urandom(10**2)
    p = store.proxy(file_val)
    print(type(p))
    future = gce.submit(monitor, p)
    print(future.result())
