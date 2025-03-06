'''
Assignment 4
CYBV 312 SPRING 2025
Your Jordan, Lanham
Due on 3/9/25
'''

# Python Standard Libaries 
import os
import hashlib
from pathlib import Path
import time

# Python 3rd Party Libraries
from prettytable import PrettyTable     # pip install prettytable

def hash_filecontent(filePath):
    '''
    Given a file name, read the file data, assuming the file data is binary, 
    and hash the file content using sha256
    
    Parameters:
    - filepath(str): filename used to access the file data
    
    Returns:
    str: the hexdecimal hash value produced based on the file data using sha256 
         if the file can be opened and read
    None: otherwise 
    '''

    result =None
    print("\nAttempting to hash file:", filePath)
    pass

def get_filemetadata(filePath):
    '''
    Given a file path, collect the metadata that describe the file
    
    Parameters:
    - filepath(str): the file path used to access the file
    
    Returns:
    tuple: the return tuple is composed of the abosolute path, 
           file size, hashvalue of the file content, a list of MAC times
           if the file can be opened 
    None: otherwise
    '''
    try:
        absPath  = os.path.abspath(filePath)
        fileSize = os.path.getsize(absPath)
        pass
    except Exception as err:
        pass

# main function
def main():
    print(Path.cwd())
    targetFolder = input("Enter Target Folder: ")
    
    # Start walking the folder
    
    print("Walking: ", targetFolder, "\n")
    
    #You will need to add more columns to the PrettyTable
    tbl = PrettyTable(['FilePath','FileSize'])  
    
    for currentRoot, dirList, fileList in os.walk(targetFolder):
    
        for nextFile in fileList:
    
            #Besides the absolute path and file size, you will need to add
            #code to get the MAC Times and convert them to human readable form
            #as well as creating a SHA-256 Hash value for each file.
            #Hint: call the function get_filemetadata   try:
            fullPath = os.path.join(currentRoot, nextFile)
            pass
    
            #You will need to add the variables that you stored the MAC and HASH
            #Code to add data to the pretty table
    
    tbl.align = "l" # align the columns left justified
    
    # display the table
    print (tbl.get_string(sortby="FileSize", reversesort=True))
    
    # Display the table sorted by Last Modified Date (Oldest to Newest) and AbsPath
    
    
    #The following code will create a CSV file with the saved information
    #We will talk more about this in the next couple of weeks.
    ''' Create CSV File Name based on date and time '''
    now = time.time()
    timeString = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime(now))
    csvFileName = "A4LastName"+timeString+".csv"
    print(csvFileName)
    
    ''' Open the CSV File and write the contents'''
    with open(csvFileName, 'w') as outFile:
        csvOut = tbl.get_csv_string(sortby="FilePath")
        outFile.write(csvOut)
    
    print("\nScript-End\n")

    
if __name__== "__main__":
    main()

