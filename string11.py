decimal = int(input("Enter a decimal number : "))

binary = ""
if decimal == 0:
    binary = "0"
while decimal > 0:
    binary = str(decimal%2) + binary 
    decimal = decimal // 2

print("Binary : ", binary)

# Enter a decimal number : 10
# Binary :  1010