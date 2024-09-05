import os

# Input file path
input_file_path = os.path.join(os.path.expanduser("~"), "Desktop", "input.txt")

# Non-toxic file path
non_toxic_file_path = os.path.join(os.path.expanduser("~"), "Desktop", "non_toxic.txt")

# Epitope file path
epitope_file_path = os.path.join(os.path.expanduser("~"), "Desktop", "epitope.txt")

# Output file path
output_file_path = os.path.join(os.path.expanduser("~"), "Desktop", "output.txt")

# Open input file and non-toxic output file
with open(input_file_path, 'r') as input_file, \
     open(non_toxic_file_path, 'w') as non_toxic_file:

    # Iterate over input file rows
    for row in input_file:
        # If the row contains the word "non-toxic", write it to the non-toxic output file
        if 'non-toxic' in row:
            non_toxic_file.write(row)

# read the row numbers from non-toxic file
with open(non_toxic_file_path, 'r') as non_toxic_file:
    row_numbers = [int(line.split()[0]) for line in non_toxic_file]

# select rows from epitope file
selected_rows = []
with open(epitope_file_path, 'r') as epitope_file:
    for i, line in enumerate(epitope_file):
        if i+1 in row_numbers:
            selected_rows.append(line)

# write selected rows to output file
with open(output_file_path, 'w') as output_file:
    output_file.writelines(selected_rows)

# read the row numbers from non-toxic file
with open(non_toxic_file_path, 'r') as non_toxic_file:
    row_numbers = [line.split()[-1] for line in non_toxic_file]

# select rows from output file and add row numbers from non-toxic file
final_rows = []
with open(output_file_path, 'r') as output_file:
    for i, line in enumerate(output_file):
        row_number = row_numbers[i]
        final_rows.append(f"{row_number}\t{line}")

# write final rows to output file
with open(output_file_path, 'w') as output_file:
    output_file.writelines(final_rows)

print("Done!")
