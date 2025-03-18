import math
#circumference

radius = float(input("Enter the radius of the circle: "))

circumference = 2 * math.pi * radius
circumference = round(circumference, 2)

print(f"The circumference is {circumference}m")

#Area
radius = float(input("Enter the radius of the circle: "))

area = math.pi * radius ** 2
area = round(area, 2)

print(f"The area is {area}m²")

#Hypoteneuse
base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))

hypoteneuse = math.sqrt(pow(base, 2) + pow(height, 2))
hypoteneuse = round(hypoteneuse, 2)

print(f"The hypoteneuse is {hypoteneuse}m")