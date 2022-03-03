def rect(x,y):
 return x*y
def circle(r):
 PI = 3.142
 return PI * (r*r)
def triangle(a, b, c):
 Perimeter = a + b + c
 s = (a + b + c) / 2
 Area = math.sqrt((s*(s-a)*(s-b)*(s-c)))
 print(" The Perimeter of Triangle = %.2f" %Perimeter)
 print(" The Semi Perimeter of Triangle = %.2f" %s)
 print(" The Area of a Triangle is %0.2f" %Area)
def parallelogram(a, b):
 return a * b;
# Python program to compute area of rectangle
l = int(input(" Enter the length of rectangle : "))
b = int(input(" Enter the breadth of rectangle : "))
a = rect(l,b)
print("Area =",a)
# Python program to find Area of a circle
num=float(input("Enter r value of circle:"))
print("Area is %.6f" % circle(num))
# python program to compute area of triangle
import math
triangle(6, 7, 8)
# Python Program to find area of Parallelogram
Base = float(input("Enter the Base : "))
Height = float(input("Enter the Height : "))
Area =parallelogram(Base, Height)
print("The Area of a Parallelogram = %.3f" %Area) 
