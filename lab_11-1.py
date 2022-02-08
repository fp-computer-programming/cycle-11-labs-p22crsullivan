# Author: CRS 02/08/21
file = open("alma_mater.txt", "r")
while True:
     line = file.readline()
     if len(line) == 0:
           break
     print (line, end="")
     print(" ")
file.close()