#Leon Kobia
#17/02/26
#Program to run quadratic equations
import math
a =float(input ("Enter the coefficient a: "))
b =float(input ("Enter the coefficient b: "))
c =float(input ("Enter the coefficient c: "))

d= b**2 - 4*a*c

if d > 0:
    root1 = (-b + math.sqrt(d)) / (2*a)
    root2 = (-b - math.sqrt(d)) / (2*a)
    print(f"The roots are real and distinct: {root1} and {root2}")
elif d == 0:
    root = -b / (2*a)
    print(f"The roots are real and equal: {root}")
else:
    real_part = -b / (2*a)
    imaginary_part = math.sqrt(-d) / (2*a)
    print(f"Complex roots:", real_part, "+", imaginary_part, "i and", real_part,"-", imaginary_part, "i")