class bicycle:
    def __init__(self):
        self.brand = ""
        self.model = ""
        self.year = 0
        self.description = ""
        self.weight_kg = 0
    
    def name(self,brand,model,year):
        self.brand = brand
        self.model = model
        self.year = year
        print(f'Brand: {self.brand}')
        print(f'Model: {self.model}')
        print(f'Year: {self.year}')


    def weight_lbs(self,kilogram):
        self.weight_kg=kilogram
        pounds=kilogram*2.2046226218
        print(f'{self.weight_kg} kilograms = {pounds} pounds')
    def set_weight_lbs(self,pounds):
        self.weight_kg=pounds/2.2046226218
        print(f'{pounds} pounds = {self.weight_kg} kilograms')


    def Description(self,description):
        self.description = description
        print(f'Description: {self.description}')
    
b1 = bicycle()
b1.name(input("Enter the bicycle's brand: "),
       input("Enter the bicycle's model: "),
       int(input("Enter the bicycle's year: ")))
b1.Description(input("Enter the description: "))
b1.weight_lbs(float(input("Enter the weight, in kilograms: ")))
b1.set_weight_lbs(float(input("Enter the weight, in pounds: ")))


b2 = bicycle()
b2.name(input("\n\nEnter the bicycle's brand: "),
       input("Enter the bicycle's model: "),
       int(input("Enter the bicycle's year: ")))
b2.Description(input("Enter the description: "))
b2.weight_lbs(float(input("Enter the weight, in kilograms: ")))
b2.set_weight_lbs(float(input("Enter the weight, in pounds: ")))
