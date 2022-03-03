def largest(n):
 list=[]
 print("Enter list elements one by one")
 for i in range(0,n):
   x=int(input())
   list.append(x)
 print("The list elements are")
 print(list)
 large=list[0]
 for i in range(1,n):
    if(list[i]>large):
      large=list[i]
 print("The largest element in the list is",large)
n=int(input("Enter the limit"))
largest(n)
