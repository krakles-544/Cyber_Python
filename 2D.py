fruits = ["apple","orange","banana","coconut"]
vegetables = ["celery", "carrots", "potatoes"]
meat = ["chicken","fish","turkey"]

groceries = [fruits, vegetables, meat]

print(groceries[0][0])
for item in groceries:
    for food in item:
        print(food, end=" ")
    print()


#Small exercise to build a phone number pad
num_pad = ((1,2,3),
           (4,5,6),
           (7,8,9),
           ("*",0,"#"))

for row in num_pad:
    for item in row:
        print(item, end=" ")
    print()