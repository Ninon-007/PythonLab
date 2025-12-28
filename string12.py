binary = int(input("Enter a binary number : "))

decimal = 0
power = 0 

while binary >0:
    decimal += binary%10 * (2**power)
    binary = binary //10
    power += 1

print("Decimal : ", decimal)


# Enter a binary number : 1010
# Decimal :  10