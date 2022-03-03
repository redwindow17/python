a=int(input("Entre a="))
b=int(input("Entre b="))
try:
 c = ((a+b) / (a-b))
#Raising Error
 if a==b:
  raise ZeroDivisionError
#Handling of error
except ZeroDivisionError:
 print ("a/b result in 0")
else:
 print (c)
