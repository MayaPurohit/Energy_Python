import os
import sys
import time 
import datetime


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





def run():
    '''Checks to see if the number of parameters on the command line are suffient. Will present usage statement if not'''
    
    # os.mkdir("/run/user/1000/transfer_files")   
    readFile(sys.argv[1]) 

    print("Finished reading files")


if __name__ == "__main__": #will not execute test function when the file is imported
    run()





