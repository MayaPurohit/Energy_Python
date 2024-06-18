from globus_compute_sdk import Executor
from globus_compute_sdk import Client
from proxystore.connectors.endpoint import EndpointConnector
from proxystore.connectors.file import FileConnector
from proxystore.proxy import Proxy
from proxystore.store import Store
import os 
import create_file


ENDPOINT_UUID = '140bdbcf-d136-48f1-9571-508cea4b7649'
ENDPOINT_CHAMELEON = "9c4f9d23-f36e-41df-ad06-a1366b78c445"

def monitor(p: Proxy):
    import os
    import subprocess
    import time

    # print("Monitor")
    # os.system("sudo powerstat -a -RDH 1 80 >globus_times.csv &")
    subprocess.run(["sudo powerstat -a -RDH 1 80 >globus_times.csv"], shell = True)
    time.sleep(10)
    data = p.resolve()
    #file_val = create_file.readAndWrite(x)
    return 'globus_times.csv'


#'c047182f-9d0b-4692-a012-5c228fc4fc6c'
store = Store('my-store', EndpointConnector(endpoints=['bdeb4393-9c2c-4e83-a910-8bac8b3d27fb']), register=True)
#store = Store('my-store', FileConnector('./proxystore-cache'), register=True)  

with Executor(endpoint_id=ENDPOINT_UUID) as gce:
    file_val = os.urandom(10**2)
    p = store.proxy(file_val)
    future = gce.submit(monitor, p)
    print(future.result())
