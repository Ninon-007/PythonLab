#Write a Python program which takes a positive integer n as input and finds the sum of cubes of all positive even numbers less than or equal to the number. 
sum = 0 
n = int(input("Enter a positive integer: "))
for i in range(2,n+1,2):
    sum += i**3
print(f"The sum of cubes of even numbers is: {sum}")