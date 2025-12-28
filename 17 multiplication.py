n = int(input("Enter a number : "))

for i in range ( 1 , n+1):
    print("Multiplication table of",i)
    for j in range ( 1 , 11):
        print(f"{i} X {j} = {i*j}")
    print() 