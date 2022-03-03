 #Asking the user to enter his/her age.
age = int(input("What is your age?"))

# Printing message of the condition when the age is less than 18 and the user is not allowed to vote.
if age < 18:
    print("Sorry you are not eligible to vote.") 

# Printing message of the condition when the age is less than 18 and the user is allowed to vote.
if age >= 18:
    print("You are eligible to vote.") 
