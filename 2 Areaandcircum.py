import math as m

radius = float(input('Enter radius of the circle: '))

area = m.pi * (radius ** 2)
circumference = 2 * m.pi * radius

print(f'Area = {area:.2f}')
print(f'Circumference = {circumference:.2f}')