import csv #necessary built-in module for parsing CSV files.

file = open('../us-500.csv')  #this is how you open a file, optional second encoding param
file_csv = csv.reader(file)   #this parses the CSV format 

people = [] #create an empty list

#loops through every row besides title rows, adds first names to list.
for row in file_csv:
	if row[0] != 'first_name':
		print('Name: ' + row[0] + ' ' + row[1]) #print first and last name
		people.append(row[0]) #add first names to a list
	
print(people) #print out the list

people_set = set(people) #create a set (unordered, no dupes) of people

