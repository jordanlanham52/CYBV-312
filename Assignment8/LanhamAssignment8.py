'''
Searching for Images with PIL
Assignment 8
Jordan Lanham
'''

import sys
import os
from PIL import Image
import logging
from prettytable import PrettyTable

def main():

    '''Modify this print statement to include your first and last name in it'''
    print("\nStarter Script - Jordan Lanham\n")

    '''Use an input statement to ask the user for what directory with images they would like to use'''
    directory = input("Enter the directory containing images: ")

    '''Display a statement about the provided directory if it is an invalid directory to walk'''
    if not os.path.isdir(directory):
        print(f"Provided path {directory} is not a valid directory.")
        return

    '''Define your Pretty Table with the headings, Path, Ext, Format, Width, Height, Mode'''
    table = PrettyTable(["Path", "Ext", "Format", "Width", "Height", "Mode"])

    '''Store the name of the log file in a variable. The log file should be LastNameImageLog.txt'''
    log_filename = "LanhamImageLog.txt"
    if os.path.exists(log_filename):
        os.remove(log_filename)
    logging.basicConfig(filename=log_filename, level=logging.INFO,
                        format='%(asctime)s %(levelname)s %(message)s')
    logging.getLogger("PIL").setLevel(logging.WARNING)

    '''The following code will be helpufl in creating your code.
    Remember this code is allowing the user to enter one file at a time
    your code will loop through a directory. Use previous examples to help.'''

    for root, dirs, files in os.walk(directory):
        for filename in files:
            path = os.path.join(root, filename)
            if os.path.isfile(path):
                ext = os.path.splitext(path)[1]
                try:
                    with Image.open(path) as im:
                        print("File Details")
                        print("Path:         ", path)
                        print("Extension:    ", ext)
                        print("Image Format: ", im.format)
                        print("Image Width:  ", im.width,  "Pixels")
                        print("Image.Height: ", im.height, "Pixels")
                        print("Image.Mode:   ", im.mode)
                        table.add_row([path, ext, im.format, im.width, im.height, im.mode])
                        logging.info("File Details")
                        logging.info("Path: %s", path)
                        logging.info("Extension: %s", ext)
                        logging.info("Image Format: %s", im.format)
                        logging.info("Image Width: %s", im.width)
                        logging.info("Image Height: %s", im.height)
                        logging.info("Image Mode: %s", im.mode)
                except Exception:
                    print("File is not a known Image Type: ", path)
            else:
                print("Path Provided is Not a File: ", path)

    '''align your table left, add a title, and print the Pretty Table sorted by Format'''
    table.align = "l"
    table.title = "Image File Information"
    table.sortby = "Format"
    print(table)

    print("Script Done")

if __name__ == "__main__":
    main()
        