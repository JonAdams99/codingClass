# Writes content from a uwer to a file

PROMPT = "enter numbers, Please - Zero to quit:"

outFilename = input("what is the name of your outpur file?")


#create a new file object, in "write" mode

dataFile = open(outFilename, "w")

i=1
while i != 0:
    userInput = input (PROMPT)
    print(userInput)
    if userInput == "0":
        i =0
    else:
        #write the user's input to the file
        print(userInput, file=dataFile)

#close the file with the method "close"
dataFile.close()