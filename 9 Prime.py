#Program to check whether the given number is prime or not  
import math as m
num = int(input("Enter a number: "))

if num<2:
    print(f"{num} is not a Prime")
else:
    prime = True
    for i in range(2,int(m.sqrt(num))+1):
        if num % i == 0:
            prime = False
            break
    if prime:
        print(f"{num} is a Prime")
    else:
        print(f"{num} is not a Prime")