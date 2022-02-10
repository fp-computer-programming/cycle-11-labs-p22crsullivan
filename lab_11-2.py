# Author: CRS 02/08/21
file = open("alma_mater.txt", "r")
while True:
     line = file.readlines()
     for lines in reversed(line):
           print(lines)