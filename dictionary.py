capitals = {"USA": "Washington DC",
            "India":"New Delhi",
            "China":"Beijing",
            "Russia":"Moscow"}

#print(capitals.get("Japan"))

#if capitals.get("China"):
 #   print("That capital exists")
#else:
 #   print("That capital does not exist!")

#capitals.update({"Germany":"Berlin"})
#capitals.update({"USA":"Detroit"})
#capitals.pop("China")
#capitals.popitem()
#capitals.clear()
#keys = capitals.keys()
#values = capitals.values()
#items = capitals.items()
#print(items)
for key, value in capitals.items():
    print(f"{key}:{value}")