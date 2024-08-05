#Read in  a file called add.txt & display if the the screen
#Make sure add.txt is in the same project

dataFile = open("textFiles/the numbe")
for line in dataFile:
    print("-", line.rstrip())
dataFile.close()


