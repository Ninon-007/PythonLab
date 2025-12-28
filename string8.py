s = str(input("Enter a string : "))
length = len(s)
result = s[:length//2][::-1] + s[length//2:][::-1]
print(result)

# Enter a string : anandu 
# anaudn