num = 5
user_role = "guest"
#print("even" if num % 2 == 0 else "odd")
user_access = "Full access" if user_role == "admin" else "Limited access"

print(user_access)