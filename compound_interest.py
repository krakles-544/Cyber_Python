principle = 0
rate = 0
time = 0

while principle <= 0:
    principle = float(input("Enter the principle amount: "))
    if principle <= 0:
        print("Principle amount must be greater than 0!")


while rate <= 0:
    rate = float(input("Enter the interest rate: "))
    if rate <= 0:
         print("Interest rate should be greater than 0!")

while time <= 0:
    time = int(input("Enter the time duration: "))
    if time <= 0:
        print("The time duration must be greater than 0!")

print(f"Principle: ${principle:,.2f}")
print(f"Rate: {rate:.2f}")
print(f"Time: {time}")

final_amount = principle * pow((1 + rate/100),time)
print(f"Total amount after {time} year/s is ${final_amount:,.2f}")

        ###orr###

principle = 0
rate = 0
time = 0

while True:
    principle = float(input("Enter the principle amount: "))
    if principle < 0:
        print("Principle amount must be greater than 0!")
    else:
        break


while True:
    rate = float(input("Enter the interest rate: "))
    if rate < 0:
        print("Interest rate should be greater than 0!")
    else:
        break

while True:
    time = int(input("Enter the time duration: "))
    if time < 0:
        print("The time duration must be greater than 0!")
    else:
        break

print(f"Principle: ${principle:,.2f}")
print(f"Rate: {rate:.2f}")
print(f"Time: {time}")

final_amount = principle * pow((1 + rate/100),time)
print(f"Total amount after {time} year/s is ${final_amount:,.2f}")