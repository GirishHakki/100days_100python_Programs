import math
a = float(input("Enter a : "))
b = float(input("Enter b : "))
c = float(input("Enter c : "))
d = b * b -4 * a * c

if d < 0:
    print("No real roots are there")
elif d==0:
    r1 = r2 = -b/(2*a)
    print("Real and Equal Roots ", r1,r2)
else:
    r1 = (-b + math.sqrt(d)) / (2 * a)
    r2 = (-b - math.sqrt(d)) / (2 * a)
    print("Real and Unequal roots are ",round(r1,2),round(r2,2))

