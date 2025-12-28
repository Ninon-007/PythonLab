s = str(input("Enter a string : "))

has_digit = any(ch.isdigit() for ch in s)
has_alpha = any(ch.isalpha() for ch in s)
has_special = any(ch in "@#$" for ch in s)
has_upper = any(ch.isupper() for ch in s)
has_lower = any(ch.islower() for ch in s)

if has_digit:
    print("Password must contain at least one number between 0 and 9")
elif has_alpha:
    print("Password must contain at least one letter between 'a' and 'z'")
elif has_special:
    print("Password must contain at least one special character from $, #, @")
elif has_upper:
    print("Password must contain at least one letter between A and Z")
elif has_lower:
    print("Password must contain at least one letter between a and z")
else:
    print("Password is valid")