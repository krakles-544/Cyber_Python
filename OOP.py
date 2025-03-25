#Object = A "bundle" of related attributes (variables) and methods (functions)

#Class = (blueprint) used to design the structure and layout of an object


class car:
    def __init__(self, model, year, color, for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale

    def drive(self):
        print(f"You drive the {self.color} {self.model}")
    def stop(self):
        print(f"You stop the {self.color} {self.model}")

car1 = car("Porsche", "2024", "black", True)


        
car1.drive() 
car1.stop()       