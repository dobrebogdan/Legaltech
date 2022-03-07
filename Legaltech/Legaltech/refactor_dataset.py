import csv
from os import listdir
file_paths = [file for file in listdir('legislatie/ro')]

for file_path in file_paths:
    with open(f'legislatie/ro/{file_path}') as f:
        content = f.read()
        lines = content.split('$Articolul ')[1:]
        formatted_lines = []
        [formatted_lines.append(f'Articolul {line}') for line in lines]
        with open(f'legislatie/ro2/{file_path}', 'w') as tsvfile:
            writer = csv.writer(tsvfile, delimiter='\t')
            writer.writerow(formatted_lines)
