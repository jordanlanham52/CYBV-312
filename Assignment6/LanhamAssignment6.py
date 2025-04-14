'''
CYBV 312 Spring 2025
Assignment 6
by Jordan Lanham
'''

# Python Standard Libaries 
import os               # Python Standard Library to interface with OS tools
import re               # Python Standard Library used for regular expressions
import logging          # Standard Library used for logging and debuggin
import platform         # Python Standard Library used for retrieving information about the platform
import socket           # Python Standard Library used to gain access to the BSD socket interface
import uuid             # Python Standard Library used to provide immutable University Unique IDentifier objects
import time
import datetime
import hashlib
import psutil   # pip install psutil
                # Proccess and system utilities for retrieving information on running processes and system utilization


def getSystemInfo():
    try:
        info={}
        info['platform']=platform.system()
        info['platform-release']=platform.release()
        info['platform-version']=platform.version()
        info['architecture']=platform.machine()
        info['hostname']=socket.gethostname()
        #info['mac-address']=':'.join(re.findall('..', '%012x' % uuid.getnode()))
        info['processor']=platform.processor()
        info['ram']=str(round(psutil.virtual_memory().total / (1024.0 **3)))+" GB"
        return info
    except Exception as e:
        logging.exception(e)
        return False


########Main Entry Point of Script##################
def main():    
    # Insert a print statement that includes your name and assignment 6
    print("Jordan Lanham Assignment 6")
    # Use your name as the prefix of the log file and remove any old logging script
    if os.path.isfile('JordanLanhamScriptLog.txt'):   # REPLACE YOURNAME with Your Name
        os.remove("JordanLanhamScriptLog.txt")
    
    # configure the python logger, Replace YOURNAME
    logging.basicConfig(filename='JordanLanhamScriptLog.txt', level=logging.DEBUG, format='%(process)d-%(levelname)s-%(asctime)s %(message)s')
    logging.info("Script Start\n")
        
    # Extend below to get user input, including investigator, organization, purpose, and scan directory at least
    investigator = input("Investigator Name:  ")   # Enter Your Name at this prompt
    organization = input("Class Code  :       ")   # Enter the Class at this prompt i.e. CYBV-312 YOUR SECTION
    user_dir = input("Please specify a directory: ")
    
    # Begin Logging Information and log necessary information to match the output in sampleScriptLog.txt
    logging.info("Investigator:  "+investigator)
    
    
    logging.info("="*40+"\n")
        
    # Get the System Information and log the system information 
    sysInfo = getSystemInfo()
    
    if sysInfo:
        ''' 
        YOUR CODE GOES HERE - Write all collected information to the log file.
        For each system info item, log the key and the value'''
        for key, value in sysInfo.items():
            logging.info(f"{key}: {value}")
        logging.info("="*40+"\n") #This line needs to appear after all displayed/logged system information 
    
    # Write a block of code that gets the start time, prints and logs a message if the directory provided is invalid   
    start_time = time.time()
    if not os.path.isdir(user_dir):
        print(f"Provided Directory: {user_dir} is not a valid directory")
        return
    # Start walking the provided directory if the provided diretory is valid
    print("Walking")
    file_count = 0
    for root, dirs, files in os.walk(user_dir):
        for file in files:
            if file_count >= 100:
                break
            file_path = os.path.join(root, file)
            try:
                file_stat = os.stat(file_path)
                hash = hashlib.sha256()
                with open(file_path, "rb") as f:
                    for chunk in iter(lambda: f.read(4096), b""):
                        hash.update(chunk)
                file_hash = hash.hexdigest()
    # Walk down the directory and process files as required 
                logging.info("File Processed:")
                logging.info(f"Path:  {file_path}")
                logging.info(f"File Size:  {file_stat.st_size}")
                logging.info(f"Last-Modified:  {datetime.datetime.fromtimestamp(file_stat.st_mtime).strftime('%Y-%m-%d %H:%M:%S')}")
                logging.info(f"Last-Accessed:  {datetime.datetime.fromtimestamp(file_stat.st_atime).strftime('%Y-%m-%d %H:%M:%S')}")
                logging.info(f"Created:  {datetime.datetime.fromtimestamp(file_stat.st_ctime).strftime('%Y-%m-%d %H:%M:%S')}")
                logging.info(f"SHA-256:  {file_hash}")
                logging.info("=" * 70) 
                file_count += 1
            except Exception as e:
                    logging.error(f"Error processing file '{file_path}': {e}")
            if file_count >= 100:
                break
    # Log ending information
    end_time = time.time()
    elapsed = end_time - start_time
    delta = datetime.timedelta(seconds=elapsed) 
    logging.info("=" * 40)
    logging.info(f"Files processed:  {file_count}")
    logging.info(f"Elapsed Time \t{delta}")
    logging.info("Status:  Script Ended")
    print("\nScript End")

if __name__ == "__main__":
    main()
