#jon adams
#07/22/24

#day 2

#Average

def average(number):

    # print(sum(number)/i)
    # print(i)
    return float(sum(number)) / (len(number))

def mangle(phrase):
    myList = []
    str = ""
    caps = phrase.upper()

    myList = list(caps)

    myList.pop(3)
    myList.pop(-3)
    print(myList)
    str = str.join(myList)
    print(str)

    return str

def count_e(listStrings):

    # ---More elegant way of counting Upper and Lower case Vowels---

    # to count all of the E,e in list: for v in listStrings:
    #                                       var = += string.upper().count("E")

    # upp_vowel = 0
    # low_vowel = 0
    #
    # for string in listStrings:
    #     for v in "AEIOU":
    #         upp_vowel += string.count(v)
    #     for v in "aeiou":
    #         low_vowel += string.count(v)
    # return upp_vowel, low_vowel

    j=0
    k=0
    l=0
    m=0

    myList =[]
    for i in listStrings:
        # print (i)
        myList = myList + list(i)

    for n in myList:

        if (n >= 'A' and n <= 'Z') :
            j += 1
        if (n >= 'a' and n <= 'z') :
            k = k+1
        if (n == 'A' or n == 'E' or n == 'I' or n == 'O' or n == 'U'):
            l += 1
        if (n == 'a' or n == 'e' or n == 'i' or n == 'o' or n == 'u'):
            m += 1

    return j, k, l, m

def main():

    # number = []
    # for i in range(20):
    #     number.append(eval(input("please input a number: ")))
    # print(average(number))

    # print(mangle("hellothere"))
    # print(mangle("42 degrees Celsius"))
    # print(mangle("eeeeeee"))

    print("the", count_e(["hi", "hello", "EEK!"]))
    print("second", count_e(["hi", "hello", "OOOOF!"]))

main()