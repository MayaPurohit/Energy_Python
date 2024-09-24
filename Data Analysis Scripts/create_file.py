'''Maya Purohit
BigDataX REU 2024
The purpose of this file is to write large files in order to determine the energy used by the machine when using LUSTRE
How to run: python3 file_read_write.py <DIRECTORY_NAME> <NUMFILES>
'''

import os
import tempfile
import sys
#import matplotlib.pyplot as plt
import time 
from datetime import datetime
import subprocess


def readFile(filepath):
    '''Iterates through all of the files in a directory and reads them.

    Parameters:
    -----------
    filepath: str.
        str to represent the filepath of the directory that the files to read are stored in (will be temporary)
     '''
    #for each file that was added to the temporary directory       
    for filename in os.listdir(filepath): 
        #open each file and read them in
        with open(filepath + "/"+filename, "rb") as file:
            #print(os.path.getsize(filepath + "/"+filename)) #used to see the size of the files that were generated 
            print(f"Reading File size = {os.path.getsize(filepath + '/'+filename)}, time = {datetime.datetime.now()}")
            file.seek(0)
            #read the files 
            file.read() 
            # time.sleep(10)


def writeFile(filepath, filename, power10, original_time):
    ''' Creates temporary files of a given size to be stored in the filepath that is inputted 

    Parameters:
    -----------
    filepath: str.
        str to represent the filepath of the directory that the files should be written to (will be a temporary directory)
    power10
        int used to determine the number of bytes the file will be. The file created will be (10 ** power10) bytes large  
    '''

    time_format = '%Y-%m-%d %H:%M:%S'
    original_time_int = int(original_time.timestamp())

    current_time = datetime.now()
    current_time_int = int(current_time.timestamp())

    print(f"Writing File size = {10 ** power10}, time = {current_time}, time elapsed: {current_time_int - original_time_int}")
    full_path = os.path.join(filepath, filename)
    with open(full_path, 'wb+') as f:
        f.write(os.urandom(10 **power10))
    return f

    


def write(filepath, numFiles): 
    ''' Driver function to write files of different sizes and read them

    Parameters:
    -----------
    numFiles: int
        int to represent the number of files to be generated and their size (10^0 byte - 10^numFiles byte files will be created) 
    '''

    os.path.join(filepath, "transfer_files")

    os.makedirs(os.path.join(filepath, "transfer_files"), exist_ok=True)   

    og_time = datetime.now()
    print("Writing files: ", og_time)
    #write files of different sizes
    for j in range(3):
        print("Sleeping for Ten Seconds: ")
        time.sleep(10)
        # for i in range(int(numFiles) + 1): 
            # writeFile("file_" + str(i) + "_" + str(j), i, og_time)
        writeFile(os.path.join(filepath, "transfer_files"), "file_" + numFiles, int(numFiles), og_time)


def run():
    '''Checks to see if the number of parameters on the command line are suffient. Will present usage statement if not'''

    write(sys.argv[1], sys.argv[2]) #calls the function to run the program


if __name__ == "__main__": #will not execute test function when the file is imported
    run()
