s = str(input("Enter a string : "))
result = ""
if " " in s: # if s.find(" ") != -1:   ;it gives the first index of the space
    result = s.replace(" ","*")
else:
    result = "$" + s + "$"

print(result)

# Enter a string : python lab
# python*lab

# Enter a string : python
# $python$