import os
import sys
import time 
from datetime import datetime


def readFile(filepath, original_time):
    '''Iterates through all of the files in a directory and reads them.

    Parameters:
    -----------
    filepath: str.
        str to represent the filepath of the directory that the files to read are stored in (will be temporary)
     '''
    #for each file that was added to the temporary directory   
    time_format = '%Y-%m-%d %H:%M:%S'
    original_time_int = int(original_time.timestamp())

    for i in range(3):
        print("Sleeping for 10 seconds: ")
        time.sleep(10)
        for filename in os.listdir(filepath):
            #open each file and read them in
            with open(filepath + "/"+filename, "rb") as file:

                #print(os.path.getsize(filepath + "/"+filename)) #used to see the size of the files that were generated 
                current_time = datetime.now()
                current_time_int = int(current_time.timestamp())

                print(f"Reading File size = {os.path.getsize(filepath + '/'+filename)}, time = {current_time}, time elapsed: {current_time_int - original_time_int}")
                file.seek(0)
                #read the files 
                file.read() 
                





def run():
    '''Checks to see if the number of parameters on the command line are suffient. Will present usage statement if not'''
    
    og_time = datetime.now()
    print("Reading files: ", og_time)
    readFile(sys.argv[1], og_time) 

    print("Finished reading files")


if __name__ == "__main__": #will not execute test function when the file is imported
    run()






        




