import csv

with open('test.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print(f"\t{row[0]} {row[1]}'s birthday is in {row[2]}.")
            line_count += 1
            