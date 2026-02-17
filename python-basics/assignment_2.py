#Leon Kobia
#16/02/26
#Program to make a table showing sin,cos and tangent

import math

# Table header
print("+---------+------------+------------+------------+")
print("| Degree  |    Sine    |   Cosine   |   Tangent  |")
print("+---------+------------+------------+------------+")

for degree in range(-180, 181, 30):
    rad = math.radians(degree)
    
    sine = math.sin(rad)
    cosine = math.cos(rad)
    
    # Handle undefined tangent (cosine very close to 0)
    if abs(cosine) < 1e-10:
        tangent = "Undefined"
        print(f"| {degree:>7} | {sine:>10.4f} | {cosine:>10.4f} | {tangent:^10} |")
    else:
        tangent = math.tan(rad)
        print(f"| {degree:>7} | {sine:>10.4f} | {cosine:>10.4f} | {tangent:>10.4f} |")

print("+---------+------------+------------+------------+")


