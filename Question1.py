phoneDirectory={}
print("WELCOME TO THE GRANN'S PHONE DIRECTORY \n1.Add a record\n2.Search a record\n3.Update a record\n4.Sort the record alphabetically.\n5.Delete a record\n6.Quit ")
x = int(input("Enter Your Choice: "))
i=1
while x!=6:
   
    if x==1:
         a=input("Enter Name ")
         b=int(input(" Enter your 10-digit phone number: "))
         phoneDirectory.update({a:b})

        
  
        
    elif x==2:

        c=(input("Which record do you want to search "))
        if c in phoneDirectory:
            print(c,":",phoneDirectory[c])
            print(phoneDirectory)
        else:
            print("No Record here ")         

    elif x==3:
         a=input("Enter Name ")
         b=int(input(" Enter your 10-digit phone number: "))
         phoneDirectory.update({a:b})
         print(phoneDirectory)
    
    elif x==4:
         phoneDirectory.sort()
         print(phoneDirectory)

    elif x==5:
          

     d=(input("What record do you want to delete "))
     if d in phoneDirectory:
             del phoneDirectory[d]
             
             print(phoneDirectory)
     else :
             print("No Record here")   

    print("WELCOME TO THE GRANN'S PHONE DIRECTORY \n1.Add a record \n2.Search a record\n3.Update a record\n4.Sort the record alphabetically.\n5.Delete a record\n6.Quit ")
    x = int(input("Enter Your Choice: "))
   




   




    

       



        



