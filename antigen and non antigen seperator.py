import os
import tkinter as tk
from tkinter import filedialog

# get the path to the desktop folder
desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')

# create a Tkinter window
root = tk.Tk()

# hide the main window
root.withdraw()

# open a file dialog box to select the input file
file_path = filedialog.askopenfilename()

# open the input file for reading
with open(file_path, 'r') as input_file:
    # read all the lines into a list
    lines = input_file.readlines()

# create an empty list to hold the non-antigen lines
non_antigen_lines = []

# loop through all the lines in the input file
for line in lines:
    # if the line does not contain the word "NON-ANTIGEN"
    if "NON-ANTIGEN" not in line:
        # add it to the list of non-antigen lines
        non_antigen_lines.append(line)

# create a list of the antigen lines
antigen_lines = [line for line in lines if "NON-ANTIGEN" in line]

# determine the output file names based on the contents of the lines
if non_antigen_lines:
    # if there are non-antigen lines, save them to a file named "non-antigen.txt"
    non_antigen_file_name = "non-antigen.txt"
else:
    # if there are no non-antigen lines, save the original lines to a file named "antigen.txt"
    non_antigen_file_name = "antigen.txt"

if antigen_lines:
    # if there are antigen lines, save them to a file named "antigen.txt"
    antigen_file_name = "antigen.txt"
else:
    # if there are no antigen lines, save the original lines to a file named "non-antigen.txt"
    antigen_file_name = "non-antigen.txt"

# save the non-antigen lines to a file with the appropriate name
with open(os.path.join(desktop_path, non_antigen_file_name), 'w') as output_file:
    # write all the non-antigen lines to the file
    output_file.writelines(non_antigen_lines)

# save the antigen lines to a file with the appropriate name
with open(os.path.join(desktop_path, antigen_file_name), 'w') as output_file:
    # write all the antigen lines to the file
    output_file.writelines(antigen_lines)

# print a message to confirm that the program has finished
print("Files processed successfully!")
