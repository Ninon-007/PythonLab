#Program to find the Sum of the digits of a number 

number = int(input("Enter a number: "))
sum = 0
while number > 0:
    sum += number % 10
    number = number // 10
print(f"The sum of the digits is: {sum}")
