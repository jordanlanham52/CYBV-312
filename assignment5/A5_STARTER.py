''' 
CYBV 312 Spring 2025
Assignment #5
by Jordan Lanham
'''

# Standard Library Imports
import re
import os
from pathlib import Path

# 3rd Party Library Imports
from prettytable import PrettyTable   #pip install prettytabel

def searchValues(patterns, bdata):
    """
    Search values in the given binary data using all the specified regular expression patterns.

    This function applies the regex (pattern) list and collects all matches into a list of 
    matched data values. Each item in the returned list is an inner list that contains matches  
    for the corresponding pattern.  For example, if the patterns includes two re.Pattern objects:
    one is for an URL and the second is for an IPV4 address, the return value is a list 
    that contains two lists: the list of matched URL strings and the list of matched IPV4 addresses

    Args:
        pattern (re.Pattern): A regular expression pattern for matching URLs.
        bdata (bytes): The binary data in which to search for matching URLs.

    Returns:
        list of lists: A list of lists, each of which contains items that match the corresponding pattern
    
    """
    matches = []
    for pattern in patterns:
        found = pattern.findall(bdata.decode(errors='ignore'))
        matches.append(found)
    return matches


def createTable(values, title, headingStr):
    """
    Create, sort, and display a PrettyTable object based on the provided list of string values.

    This function creates a table with two columns: headingStr and "Occurrences". Each
    unique value from the values is added as a row in the table, along with the number
    of times it appears in the input list. After creating the table, it sorts the 
    rows in descending order based on the "Occurrences" column and then displays the table.


    Args:
        values (list of str): A list of strings to include in the table.

    Returns:
        PrettyTable: A table object containing each unique value and the number of
        times it appears in the input list.
    """
    table = PrettyTable()
    table.title = title
    table.field_names = [headingStr, "Occurences"]
    counter = {}

    for val in values:
        counter[val] = counter.get(val, 0) + 1

    for val, count in counter.items():
        table.add_row([val, count])

    table.sortby = "Occurences"
    table.reversesort = True

    print(table)
    return table

def writeToHTMLFile(tblVAL, filePath):
    """
    Convert the given PrettyTable object to HTML and save the resulting HTML to a file.

    This function takes a PrettyTable object, renders it as HTML, and writes the HTML
    content into a specified file path. The output file is an .html file for storing HTML content.

    Args:
        tblVAL (PrettyTable): The table object to be converted into HTML.
        file_path (str): The path (including filename) where the HTML output will be saved.

    Returns:
        None: The function writes the HTML content to the specified file path and does not
        return a value.


    """
    with open(filePath, "w") as f:
        f.write(tblVAL.get_html_string(sortby="Occurences", reversesort=True))

def process_file(filename, patterns, chunkSize):
    """
    Process the given file to search for URLs and IP addresses using the specified patterns.

    Args:
        filename (str): The name of the file to process.
        patterns (list): A list of regular expression patterns to search for.
        chunkSize (int): The size of chunks to read from the file.

    Returns:
        None: This function prints the results and writes an HTML file with the PrettyTable outputs.
    """
    # Initialize empty lists for URLs and IP addresses
    allURLs = []
    allIPs = []
    print(f"\nProcessing file: {filename}")

    try:
        # Open the file as 'rb' (read binary)
        with open(filename, "rb") as targetFile:
            # Loop through the file chunks and search for the URLs and IP addresses
            while chunk := targetFile.read(chunkSize):
                results = searchValues(patterns, chunk)
                allURLs.extend(results[0])
                allIPs.extend(results[1])

        # Convert byte strings to regular strings
        allURLs = [url.decode(errors='ignore') if isinstance(url, bytes) else url for url in allURLs]
        allIPs = [ip.decode(errors='ignore') if isinstance(ip, bytes) else ip for ip in allIPs]

        # Print a message to let user know how many URLs are discovered
        print(f"Total URLs found: {len(allURLs)}")
        # Create a PrettyTable and display all discovered URLs
        urlTable = createTable(allURLs, f"Discovered URLs in {filename}", "URL")

        # Print a message to let user know how many IPV4 addresses are discovered
        print(f"Total IP Addresses found: {len(allIPs)}")
        # Create a PrettyTable and display all discovered IPV4 addresses
        ipTable = createTable(allIPs, f"Discovered IP Addresses in {filename}", "IP Address")

        print(f"\nCreating HTML File for {filename}")
        # Write the two table data to a single HTML file
        htmlFileName = filename.split('.')[0] + "A5Result.html"
        with open(htmlFileName, "w") as html_file:
            html_file.write(urlTable.get_html_string())
            html_file.write("<br><br>")
            html_file.write(ipTable.get_html_string())
        print(f"HTML file {htmlFileName} created successfully.")
    except Exception as err:
        print(f"Error processing {filename}: {err}")

def main():
    # Display student name and assignment number
    print("Jordan Lanham - Assignment #5\n")

    # Set up two regular expressions: the first is for a URL and the second for IPV4 addresses
    urlPattern = re.compile(r"https?://[^\s\"'>]+")
    ipPattern = re.compile(r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b")
    patterns = [urlPattern, ipPattern]

    # Create a variable that will hold the value of the chunk size
    chunkSize = 2048

    # Process each file: first fake_data.txt and then mem.raw
    for filename in ["fake_data.txt", "mem.raw"]:
        process_file(filename, patterns, chunkSize)
    
    print("\nScript Complete")

if __name__ == "__main__":
    # Put the main logic here  
    main()