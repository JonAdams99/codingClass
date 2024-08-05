#jon adams
#08/03/24

import statistics

listFall =[]
listSpring = []

# Mean, Median, STD of a CVS file
# Mean: average of numbers  print(statistics.mean([1, 3, 5, 7, 9, 11]))
# Median: the middle number, if 2 numbers average of the 2 numbers  print(statistics.median([1, 3, 5, 7, 9, 11, 12]))
# Standard Deviation; print(statistics.stdev([1, 30, 50, 100]))

# funciton to access and read each line of the file

# seperate each line into Fall and Spring semesters
# calculate mean, median, STD
#  print ot user

#Read in  a file called add.txt & display if the the screen
#Make sure add.txt is in the same project

# def loop through listFiles = [test1.txt, test2.txt, test3.txt]
    #call def count lines
        #call def count words
# print(fileName : #lines "lines," #words "words")



def countThing(listFiles):

    countLinesTotal = 0
    countWordsTotal = 0
    i=0

    for i in range(len(listFiles)):
        countLines =0

        countLines2, countWords = countLine(listFiles[i])
        
        countLines = countLines2+countLines
        print(listFiles[i]," : ", countLines, "lines,", countWords, "words" )

        countLinesTotal = countLinesTotal + countLines
        countWordsTotal = countWordsTotal + countWords

        
    return countLinesTotal, countWordsTotal

def countLine(fileName):
   
    num = 0
    num2 = 0
    dataFile = open("textFiles/"+fileName)

    for line in dataFile:
        countWord(line)

    dataFile.close()


    return listFall, listSpring
def countWord(line):
    num = ""
  
    i=0

    num = (line.split(","))
    num[-1] = num[-1].strip()
    # num = line.rstrip().split(",")
    for i in num:
       # print(i)
       if i == "Fall 2016":
            # listFall.append(eval(num[2]))
           listFall.append(num[2])
       elif i == "Spring 2016":

           listSpring.append(num[2])


    return listFall, listSpring

def main():
    
    #print(listFall)
    
    cvsFile = "sample_grades.csv"

    countLine(cvsFile)
    listF = [eval(i) for i in listFall]
    listS = [eval(i) for i in listSpring]

    print("          Fall 2016     Spring 2016")
    print("Mean:       ", ("%.2f" % statistics.mean(listF)),"       ", ("%.2f" % statistics.mean(listS)))
    print("Median:     ", ("%.2f" % statistics.median(listF)),"       ", ("%.2f" % statistics.median(listS)))
    print("STD:        ", ("%.2f" % statistics.stdev(listF)),"        ", ("%.2f" % statistics.stdev(listS)))
    #print("Total: ", countLinesTotal, "lines,", countWordsTotal, "words" )
main()