#def full_name(*args):
 #   for arg in args:
  #      print(arg, end=" ")

#full_name("Samuel", "Nduati", "Mwaura")

def print_address(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}:{value}")

print_address(street="132 fake street", 
               city="Detroit", 
               state="MI",
               zip="0000")