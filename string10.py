# Write a python program to check
# validity of password given by user.
# Password should satisfy following criteria :-

# Contains atleast one letter between
# 'a' and 'z'.

# Contains atleast one number between
# 0 and 9.

# Contains atleast one letter between
# A and Z.

# Contains atleast one special character
# from $, #, @
# Minimum length of password : 6

s = str(input("Enter a password : "))

has_digit = False
has_special = False
has_upper = False
has_lower = False

for ch in s:
    if ch.isdigit():
        has_digit = True
    elif ch.islower():
        has_lower = True
    elif ch.isupper():
        has_upper = True
    elif ch in "$#@":
        has_special = True

if len(s) < 6:
    print("Minimum length of password : 6")
elif not has_lower:
    print("Contains atleast one letter between 'a' and 'z'.")
elif not has_digit:
    print("Contains atleast one number between 0 and 9.")
elif not has_upper:
    print("Contains atleast one letter between A and Z.")
elif not has_special:
    print("Contains atleast one special character from $, #, @")
else:
    print("Password is valid")
