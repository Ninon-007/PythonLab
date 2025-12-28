#Python program to find the sum of even numbers from N given numbers 

sum = 0
N = int(input("Enter the number of elements: "))
for i in range(N):
    num = int(input(f"Enter {i+1}th number: "))
    if num % 2 == 0:
        sum += num
print(f"The sum of even numbers is: {sum}")
    