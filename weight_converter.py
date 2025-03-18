weight = float(input("Enter your weight: "))
unit = input("Kilograms(kg) or Pounds(lbs): ")

if unit == "kg":
    converted = weight * 2.20462
    print(f"Your weight is {round(converted, 2)}lbs")
elif unit == "lbs":
    converted = weight / 2.20462
    print(f"Your weight is {round(converted, 2)}kg")
else:
    print("Invalid unit")