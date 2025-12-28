#Program that accepts the length of three sides of a triangle as input and determine whether or not the triangle is a right angled triangle

a = int(input("Enter the length of side a: "))
b = int(input("Enter the length of side b: "))
c = int(input("Enter the length of side c: "))

x , y , z = sorted([a , b , c])

if x**2 + y**2 == z**2:
    print("The triangle is a right angled triangle")
else:
    print("The triangle is not a right angled triangle")