# Author: CRS 02/08/21
# Create file variable
file = open("alma_mater.txt", "r")
# Create while statement to edit file
while True:
     line = file.readline()
     if len(line) == 0:
           break
     print (line, end="")
     print(" ")
     # Close the file
file.close()