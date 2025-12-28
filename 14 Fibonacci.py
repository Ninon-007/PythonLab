#Generate first 10 Fibonacci numbers 
a , b = 0 , 1

print(a)
print(b)
for i in range(2,10):
    a , b = b , a+b
    print(b)