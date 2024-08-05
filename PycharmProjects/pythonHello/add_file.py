#Read in  a file called add.txt & display if the the screen
#Make sure add.txt is in the same project

dataFile = open("add.txt")
print (dataFile)
for line in dataFile:

    print(line.rstrip())
dataFile.close()