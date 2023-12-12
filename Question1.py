phoneDirectory={}
print("WELCOME TO THE GRANN'S PHONE DIRECTORY \n1.Add a record \n2.Search a record\n3.Update a record \n4.Sort the record alphabetically \n5.Delete a record\n6.Quit ")
x = int(input("Enter Value: "))
i=1
while x!=6:
   
   if x==1:
       if x==1:
         a=input("What is the name! ")
         b=int(input(" What is the phone number "))
         phoneDirectory.update({a:b})
       else:
        print()


   elif x==2:
     c=(input(" Search a record "))
     if c in phoneDirectory:
            print(c,"-",phoneDirectory[c])
            print(phoneDirectory)
     else:
            print("Not Found") 



   elif x==3:
     d=(input("Whats to update"))
     if len(phoneDirectory)>=0:
                     print("Nothing to Update")
     else:
        phoneDirectory.update({a:b})   



   elif x==4:
     

      
    print("WELCOME TO THE GRANN'S PHONE DIRECTORY \n1.Add a record \n2.Search a record\n3.Update a record \n4.Sort the record alphabetically \n5.Delete a record\n6.Quit ")
    x = int(input("Enter Value: ")) 
   