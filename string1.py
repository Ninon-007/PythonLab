s = str(input("Enter a string : "))
result = ""

result += "".join((ch for ch in s if ch not in "aeiouAEIOU"))
print(f"Result : {result}")


# Enter a string : aeiowyk
# Result : wyk