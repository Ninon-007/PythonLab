n = int(input("Enter a number : "))

order = len(str(n))
sum = 0
temp = n
while temp>0:
    digit = temp%10
    sum += digit**order
    temp = temp//10

if sum == n:
    print(n,"is an Armstrong number")
else:
    print(n,"is not an Armstrong number")