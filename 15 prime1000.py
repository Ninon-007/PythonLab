#Print first 1000 prime numbers 
import math as m
prime = []

for i in range (2,1001):
    is_prime = True
    for j in range (2,int(m.sqrt(i))+1):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        prime.append(i)
print(prime)