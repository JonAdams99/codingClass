#jon adams
#07/31/24
# While Loops
import re


def average_neg_evens(listNum):
    i = 0
    number = 0
    num=0
    num2=0

    while i < len(listNum):

        if(listNum[i] < 0 and listNum[i] %2 ==0):
            num = num + listNum[i]
            num2 += 1

            number = num / num2

        i+=1

    return number

def count_letter(listString, let):

    count=0

    i=0

    while i < len(listString):
        str = listString[i].lower().count(let)

        count = count + str

        i+=1

    return count

def main():

    print((average_neg_evens([0, 1, 2, -2, -3, -4, 3, 4])) == -3)
    list = ["HELLO", "goodbye", "1234 Oooh!"]
    print("count:", count_letter(list, "o"))

main()



