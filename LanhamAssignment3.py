'''
Assignment 3 CYBV 312
Jordan, Lanham
Due on 2/23/25
'''
import time
import hashlib
import itertools
from prettytable import PrettyTable 

def generate_hash(password):
    MD5Hash = hashlib.md5(password.encode())
    print(MD5Hash.hexdigest())
    return 

def brute_force_password(target_hash, charset, max_length):
    """
    Attempts to discover the password for a given hash using brute force.
    Parameters:
    - target_hash (str): The hash digest of the target password.
    - charset (str): The set of characters to use for generating password combinations.
    - max_length (int): The maximum length of the password to attempt.

    Returns:
    - str: The discovered password if found, or None if not found.
    """
    # Iterate through all possible lengths up to max_length
    for length in range(1, max_length + 1):
        # Generate all combinations of the given length
        for combination in itertools.product(charset, repeat=length):
            # Join the combination to form a password
            pass
            # Generate the hash of the candidate password
            pass
            # Check if the hash matches the target hash
            pass 


    return None  # Password not found within the given constraints

def defineRT(charset, min_lenth, max_length):
    """
    Creates a rainbow table with generated passwords and md5 hash values.
    Each password uses only a limited string of characters in limited length.  
    Parameters:
    - charset (str): The set of characters to use for generating password combinations.
    - max_length (int): The maximum length of passwords.
    - min_length (int): The minimum length of passwords.

    Returns:
    - dict: The dictionary composed of pairs <md5 hash digest, password>
    """    
    rainbowTable = {}      
    #more code to add
    pass
    return rainbowTable
            
def displayRT(rainbowTable):
    '''
    Display the size of the rainbow table and then display ten rows in a pretty table
    Parameters:
    - rainbowTable (dict) : The rainbow table to be displayed 
    Returns:
    - None
    '''
    pass
    
    
def main():
    pw = 'aa@12!'
    
    #create a variable target to store the md5 hash of pw
    target = 'dummy' #should update this target hash value
    
    #Modify the below code to test brute_force_password and document the time to discover the password
    charset = 'ab12!@'
    found = brute_force_password(target, charset, 8)

    #Modify the below code to test defineRT and document the time to construct the rainbow table
    rt = defineRT(charset, 4, 6)
    
    #Write more code to check how many seconds used to discover the password given the target hash using the rainbow table 

    #Call displayRT to test the function definition
      

if __name__=='__main__':
    main()
    