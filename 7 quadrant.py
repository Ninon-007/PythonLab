#Input a point and find the quadrant of the point

x = int(input("Enter the x coordinate: "))
y = int(input("Enter the y coordinate: "))

if x > 0 and y > 0:
    print("1st quadrant")
elif x < 0 and y > 0:
    print("2nd quadrant")
elif x < 0 and y < 0:
    print("3rd quadrant")
elif x > 0 and y < 0:
    print("4th quadrant")
elif x == 0 and y == 0:
    print("Origin")
else:
    print("Axis")
