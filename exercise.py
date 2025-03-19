#validate user input exercise
#1. username shouldn't be more than 12 characters
#2. username must not contain spaces
#3. usename must not include digits

#1.
username = input("Enter your username: ")

if len(username) > 12:
    print("Usename must be less than 12 characters!")
else:
    print(f"Hello {username}")

#2.

username = input("Enter your username: ")
 
if username.find(" ") != -1:
    print("Username must not include spaces!")
else:
    print(f"Hello {username}")
               ##or##
if " " in username:
    print("Username must not include spaces!")
else:
    print(f"Hello {username}")

#3.

username = input("Enter your username: ")

if not username.isalpha():
    print("Username must not include digits!")
else:
    print(f"Hello {username}")