# Author: CRS 02/08/21
# Create file variable
file = open("alma_mater.txt", "r")
# Create while statement to edit file
while True:
     line = file.readlines()
     for lines in reversed(line):
           print(lines)