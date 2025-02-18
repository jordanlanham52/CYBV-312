'''
Assignment 3 CYBV 312
Jordan Lanham
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
    # Iterate through all possible lengths up to max_length
    for length in range(1, max_length + 1):
        # Generate all combinations of the given length
        for combination in itertools.product(charset, repeat=length):
            # Join the combination to form a password
            potentialPassword = "".join(combination)
            # Generate the hash of the candidate password
            potentialHash = hashlib.md5(potentialPassword.encode())
            potentialHash = potentialHash.hexdigest()
            # Check if the hash matches the target hash
            if potentialHash == target_hash:
                print(f"The password is {potentialPassword} with the hash {potentialHash}") 
                break
    return None  # Password not found within the given constraints

def defineRT(charset, min_lenth, max_length):
    rainbowTable = {}      
    for length in range(min_lenth, max_length):
        for combination in itertools.product(charset, repeat=length):
            password = "".join(combination)
            hash = hashlib.md5(password.encode()).hexdigest()
            rainbowTable[hash] = password
    return rainbowTable
        
def displayRT(rainbowTable):
    print(f"Rainbow table size: {len(rainbowTable)} entries")
    table = PrettyTable(["MD5 Hash", "Password"])
    for i, (hash_value, password) in enumerate(rainbowTable.items()):
        if i >= 10:  
            break
        table.add_row([hash_value, password])
    print(table)
    
    
def main():
    pw = 'aa@12!'
    pwHash = hashlib.md5(pw.encode())
    #create a variable target to store the md5 hash of pw
    target = pwHash.hexdigest() #should update this target hash value
    
    #Modify the below code to test brute_force_password and document the time to discover the password
    charset = 'ab12!@'
    start = time.time()
    found = brute_force_password(target, charset, 8)
    end = time.time()
    print(f"It took {end-start} seconds to find the password using brute force")
    #Modify the below code to test defineRT and document the time to construct the rainbow table
    start = time.time()
    rt = defineRT(charset, 4, 6)
    end = time.time()
    print(f"It took {end-start} seconds to generate the table")
    #Write more code to check how many seconds used to discover the password given the target hash using the rainbow table 
    start = time.time()
    rtPassword = rt.get(target, None)
    end = time.time()
    print(f"It took {end-start} seconds to find the password using rainbow tables")
    #Call displayRT to test the function definition
    displayRT(rt)

if __name__=='__main__':
    main()
    