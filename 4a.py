bk_list=['Java','C','Cpp'] 
print("Welcome to library")
while(1):
    ch=int(input("Enter \n1. add the book to list \n2. issue a book\n3. return the book \n4. view the book list \n5. Exit\n"))
    if(ch==1):
        bk=input("enter the book name:")
        bk_list.append(bk)
        print(bk_list)
    elif(ch==2):
        ibk=input("Enter the book to issue:")
        bk_list.remove(ibk)
        print(bk_list)
    elif(ch==3):
            rbk=input("enter the book to return:")
            bk_list.append(rbk)
            print(bk_list)
    elif(ch==4):
           print(bk_list)
    else:
        break
        print("Number of book in the libarary:",len(bk_list))
        bk_list.sort()
        print("sort the book:",bk_list)
        print("part of book:",bk_list[1:3])
