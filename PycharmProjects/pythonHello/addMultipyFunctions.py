# Jon adams
# 07/22/24
#add and multipy functions in main()

def add(x,y):
    print ("i add numbers %d and %d" %(x,y))
    return x+y;

def multiply(x,y):
    print ("i multipy numbers %d and %d" %(x,y))
    return x*y;

def addLots(n):
    if n < 1:
        return 0;
    else:
        return n + addLots(n-1);

def main():
    sum = add(5,7)
    product = multiply(6,7)
    print("sum = ", sum ,"product = ", product )

    addition = addLots(6)

    #Dr Emily different function
    a = eval(input("Please enter a number: "))
    b = eval(input("Please enter a number: "))
    print("sum2 = ", add(a,b), "product2 = ", multiply(a,b), "addLots = ", addition)



main()