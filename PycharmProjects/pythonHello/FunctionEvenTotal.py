# jon adams
# 07/24/24
# Function development
def is_even(num):
    #Dr.Emily
    numG = (num% 2 == 0)
    return numG

    # boolTrue = False
    # if num % 2 == 0:
    #     boolTrue = True
    #
    # return boolTrue;

def calculate_total(meal, tax_rate, tip_rate):
    total_meal_price = 0.00

    total_meal_price = ((meal * tax_rate)+(meal * tip_rate)+(meal))

    return total_meal_price;

def hey(num):

    num = num**2
    return num;

def there(n):

    num = 0

    if n >= 0:
        num=2**n

    return num;

def are_we(num, word):

    a=""
    for i in range(num):
        sentence = ("Are we "+word+" yet? ")
        a = a + sentence

    return a;

def main():

    #Dr Emily Solution
    print("4 is Even: ", is_even(4))
    print("5 is Even: ", is_even(5))

    # num2 = 4
    # num = is_even(num2)
    #
    # if num == True:
    #     print("Even number: ", num2)
    # else:
    #     print("Odd number: ", num2)

    #print("the total meal price is: $", calculate_total(53.48, 0.07, 0.18))

    # print(hey(5))
    # print(hey(0))
    # print(hey(-3))


    # print(there(5))
    # print(there(0))
    # print(there(3))
    # print(there(-2))
    # print(there(-6))

    print(are_we(2, "there"))
    print(are_we(3, "50"))
    print(are_we(1, ""))
    print(are_we(0, "hey"))


main()



