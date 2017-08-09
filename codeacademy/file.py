#!/usr/bin/python

# when file is opened with..as clause, it will be closed 
# automatically when it goes out of scope.

with open("text.txt", "w") as textfile:
	textfile.write("Success!")

if not my_file.closed:
	my_file.close()

print my_file.closed