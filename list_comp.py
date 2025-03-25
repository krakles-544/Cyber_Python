
doubles = [x * 2 for x in range(1, 11)]

print(doubles)

fruits = ["apple", "orange", "banana", "coconut"]
fruits = [fruit.upper() for fruit in fruits]
fruit_chars = [fruit[0] for fruit in fruits]
print(fruit_chars)

grades = [85,42,79,90,56,61,30]
passing_grades = [grade for grade in grades if grade >= 60]

print(passing_grades)