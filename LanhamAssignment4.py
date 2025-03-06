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

    try:
        with open(filePath, 'rb') as file:  # Open file in binary mode
            file_data = file.read()
            result = hashlib.sha256(file_data).hexdigest()  # Compute hash
    except FileNotFoundError:
        print("Error: File not found.")
    except Exception as e:
        print(f"Error: {e}")
    
    return result

def get_filemetadata(filePath):
    '''
    Given a file path, collect the metadata that describe the file
    
    Parameters:
    - filePath (str): the file path used to access the file
    
    Returns:
    tuple: (absolute path, file size, hash value, formatted MAC times)
    '''
    try:
        absPath  = os.path.abspath(filePath)  # Get absolute file path
        fileSize = os.path.getsize(absPath)  # Get file size
        hashValue = hash_filecontent(absPath)  # Compute hash
        
        # Get raw MAC times
        mTime = os.path.getmtime(absPath)  # Last modification time
        aTime = os.path.getatime(absPath)  # Last access time
        cTime = os.path.getctime(absPath)  # File creation time (Windows) or status change (Unix)

        # Convert to human-readable format
        readable_mTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(mTime))
        readable_aTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(aTime))
        readable_cTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(cTime))

        return (absPath, fileSize, hashValue, readable_mTime, readable_aTime, readable_cTime)
    
    except Exception as err:
        print(f"Error: {err}")
        return None   
   
# main function
def main():
    print("Current working directory: ",Path.cwd())
    targetFolder = input("Enter Target Folder: ")
    if not os.path.exists(targetFolder):
        print("Error: The specified folder does not exist.")
        return
    # Start walking the folder
    
    print("Walking: ", targetFolder, "\n")
    
    #You will need to add more columns to the PrettyTable
    tbl = PrettyTable(['File Path', 'File Size (Bytes)', 'SHA-256 Hash', 'Modified Time', 'Accessed Time', 'Created Time'])
    
    for currentRoot, dirList, fileList in os.walk(targetFolder):
    
        for nextFile in fileList:
    
            #Besides the absolute path and file size, you will need to add
            #code to get the MAC Times and convert them to human readable form
            #as well as creating a SHA-256 Hash value for each file.
            #Hint: call the function get_filemetadata   try:
            fullPath = os.path.join(currentRoot, nextFile)
            metadata = get_filemetadata(fullPath)
            if metadata:
                absPath, fileSize, hashValue, mTime, aTime, cTime = metadata
                tbl.add_row([absPath, fileSize, hashValue, mTime, aTime, cTime])
                
            #You will need to add the variables that you stored the MAC and HASH
            #Code to add data to the pretty table
    
    tbl.align = "l" # align the columns left justified
    
    # display the table
    print("\n--- Sorted by File Size (Descending) ---")
    print(tbl.get_string(sortby="File Size (Bytes)", reversesort=True))
    
    # Display the table sorted by Last Modified Date (Oldest to Newest) and AbsPath
    print("\n--- Sorted by Last Modified Date (Oldest to Newest) ---")
    print(tbl.get_string(sortby="Modified Time"))
    
    #The following code will create a CSV file with the saved information
    #We will talk more about this in the next couple of weeks.
    ''' Create CSV File Name based on date and time '''
    now = time.time()
    timeString = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime(now))
    csvFileName = "A4Lanham"+timeString+".csv"
    print("\nSaving table to CSV:", csvFileName)
    
    ''' Open the CSV File and write the contents'''
    with open(csvFileName, 'w') as outFile:
        csvOut = tbl.get_csv_string(sortby="Created Time")
        outFile.write(csvOut)
    
    print("\nScript-End\n")

    
if __name__== "__main__":
    main()

