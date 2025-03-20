#1. LISTS

fruits = ["apple", "orange", "banana", "coconut"]
print(fruits[0])
print(dir(fruits))
print(help(fruits))
fruits[0] = "mango"
fruits.append("mango")
fruits.remove("apple")
fruits.insert(0, "mango")
fruits.sort()
fruits.reverse()
fruits.clear()
for x in fruits:
    print(x)

print(fruits.count("apple"))
print(len(fruits))
print("avocado" in fruits)

#2. SETS - unordered, no duplicates
fruits = {"apple", "orange", "banana", "coconut", "coconut"}
fruits.add("Mango")
fruits.remove("apple")
fruits.pop()
fruits.clear()
print(fruits)

#3. TUPLES - The only difference between tuples and lists is that tuples are faster than lists

fruits = ("apple", "orange", "banana", "coconut")