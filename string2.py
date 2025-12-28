s = str(input("Enter a string : "))
result = "".join(s[i] for i in range(len(s)) if i%2==0)
print(result)

# Enter a string : anandhu
# aadu