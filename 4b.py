def main():
# Access and modify attributes of an object
 class Car:

    # class attribute
    wheels = 4

    # initializer with instance attributes
    def __init__(self, color, style):
        self.color = color
        self.style = style

 c = Car('Black', 'Sedan')

# Access attributes
 print(c.style)
# Prints Sedan
 print(c.color)
# Prints Black

# Modify attribute
 c.style = 'SUV'
 print(c.style)
# Prints SUV
main()
