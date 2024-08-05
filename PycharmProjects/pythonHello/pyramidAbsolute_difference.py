#jon adams
#07/22/24

#day 2

#Pyramid function

# def pyramid(display, num):
#     for i in range(num+1):
#         print(display * i)
#
# def main():
#     pyramid("#", 10)
#
# main()

def abs_value(a,b):
    if (a>0 and b>0) or (a<0 and b<0):
        abs_sum = abs(a-b)
        # print (abs_sum)
        return abs_sum
    # elif a<0 and b<0:
    #     abs_sum = abs(a - b)
    #     # print (abs_sum)
    #     return abs_sum
    else:
        abs_sum = abs(a)+abs(b)
#       print("22", abs_sum)
        return abs_sum


def main():

    print("abs + ", abs_value(22,-3))
main()