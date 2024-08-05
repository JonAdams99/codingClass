# Writes content from a uwer to a file

PROMPT = "enter thbe next line in the file: "

outFilename = input("what is the name of your outpur file?")
numLines = eval(input("How many linse do you want to write? "))

#create a new file object, in "write" mode

dataFile = open(outFilename, "w")

for i in range (numLines):
    userInput = input (PROMPT)
    #write the user's input to the file
    print(userInput, file=dataFile)

#close the file with the method "close"
dataFile.close()