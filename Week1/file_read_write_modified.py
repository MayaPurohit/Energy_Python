'''Maya Purohit
BigDataX REU 2024
The purpose of this file is to write and read large files in order to determine the energy used by the machine
How to run: python3 file_read_write.py <DIRECTORY_NAME> <NUMFILES>
'''

import os
import tempfile
import sys
import matplotlib.pyplot as plt
import time 
import datetime
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


def writeFile(filepath, power10):
    ''' Creates temporary files of a given size to be stored in the filepath that is inputted 

    Parameters:
    -----------
    filepath: str.
        str to represent the filepath of the directory that the files should be written to (will be a temporary directory)
    power10
        int used to determine the number of bytes the file will be. The file created will be (10 ** power10) bytes large  
    '''
    #create temporary file
    print(f"Writing File size = {10 ** power10}, time = {datetime.datetime.now()}")
    temp = tempfile.NamedTemporaryFile(dir = filepath, delete = False)  

    #write file of size 10**power10 bytes
    temp.write(os.urandom(10 **power10))
    # time.sleep(10)

    


def readAndWrite(filesystem, numFiles): 
    ''' Driver function to write files of different sizes and read them

    Parameters:
    -----------
    filesystem: str.
        str to represent the filepath of the directory that will contain the temporary directory with the temporary files 
    numFiles: int
        int to represent the number of files to be generated and their size (10^0 byte - 10^numFiles byte files will be created) 
    run: boolean
        determines if the function will be run 
    '''

    #creates a temporary directory

    temp_dir = tempfile.TemporaryDirectory(dir = filesystem)  

    start = time.time()
    print("Writing files: ", datetime.datetime.now())
    #write files of different sizes
    for i in range(int(numFiles) + 1): 
        writeFile(temp_dir.name, i)

    # writeFile(temp_dir.name, int(numFiles))



    #will read the files in the temporary directory
    readFile(temp_dir.name) 
    print("Reading Files: ", datetime.datetime.now())

    #remove the directory and the files once we have finished reading and writing 
    # for filename in os.listdir(temp_dir.name):
    #     os.remove(temp_dir.name + "/"+filename)
    
    end = time.time()

    # #delete the directory 
    # os.removedirs(temp_dir.name) 
    print("Finished writing and reading files")


    print("Time taken: ", (end - start))

def run():
    '''Checks to see if the number of parameters on the command line are suffient. Will present usage statement if not'''
    
    if len(sys.argv) < 3:
        print("In order to run this file, please specify the file system path and the number of files you would like to generate")
        return

    readAndWrite(sys.argv[1], sys.argv[2]) #calls the function to run the program


if __name__ == "__main__": #will not execute test function when the file is imported
    run()






        




