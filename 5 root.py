import math as m

a = int(input("Enter the coeff of a : "))
b = int(input("Enter the coeff of b : "))
c = int(input("Enter the coeff of c : "))
if a==0:
    print("Invalid input")
else:
    D = b**2 - 4*a*c

    if D > 0:
        root1 = (-b+m.sqrt(D))/(a*2)
        root2 = (-b-m.sqrt(D))/(a*2)
        print(f"Roots are real and distinct : {root1:.2f} and {root2:.2f}")

    elif D==0:
        root = -b/(2*a)
        print(f"Root is real and equal : {root:.2f}")

    else:
        real = -b/(2*a) 
        imag =  m.sqrt(-D)/(2*a)
        print(f"Roots are complex : {real:.2f} + {imag:.2f}i and {real:.2f} - {imag:.2f}i")