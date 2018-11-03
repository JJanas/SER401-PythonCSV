import csv

with open('C:/Users/Burt/SER401-PythonCSV/trees.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter =',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print(f'\tIndex:{row[0]}, Girth:{row[1]}, Height:{row[2]}, Volume:{row[3]} ')
            line_count += 1
    print(f'Processed {line_count} lines.')
