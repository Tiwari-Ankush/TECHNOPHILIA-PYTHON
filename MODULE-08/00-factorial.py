def factorial(number):
    fact = 1
    if number == 0 or number==1: 
        return 1    
    else:
        for i in range(2,number+1):
            fact*=i   
    return fact


import math

if __name__ == "__main__":
    num = int(input())
    print(factorial(num))

    print(math.factorial(num))