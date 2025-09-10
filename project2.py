###############################
# Team members- Please enter your names here
# Name1:Patrick Nugent
# Name2:Saad Malik
###############################

# Modules
from Inventory import Inventory




'''------------------------------------------------------
                Main program starts here 
---------------------------------------------------------'''
# to complete
cart=Inventory()
list_books=Inventory()
list_books.initialize()

while True:
    print("Welcome to BestMedia")
    print("====================")
    print("------------------------------------------------------")
    print("1-List Inventory; 2-Info Inventory; 3-Search Inventory")
    print("4-Add Item; 5-Remove Item; 6-Inflation; 7-Shop; 8-Check-out")
    command=(input("Enter Command"))

    if command=="":
        print("Goodbye!")
        break

    if command=="1":
        print(list_books)
    
    if command=="2":
        Inventory.info(list_books)

    if command=="3":
        key_word=input("Enter a title key word:")
        Inventory.search(list_books,key_word)
    
    if command=="4":
        Inventory.add(list_books)

    if command=="5":
        Inventory.delete(list_books,int(input("Which item do you want to delete?")))

    if command=="6":
        roi=float(input("Enter inflation %:"))
        Inventory.adjust_price(list_books,roi)

    if command=="7":
        
        ct=int(input("Which item would you like to buy?"))
        Inventory.add(cart,list_books.lob[ct-1])
        
    if command=="8":
        if len(cart.lob)==0:
            print("Your cart is empty!")
        else:
            print("Current shopping cart:")
            print(cart)

            Inventory.info(cart)
            code=input("Enter your promotion code:")
            if code=="Voyage":
                Inventory.adjust_price(cart,-5)
                print("updated shopping cart")
                
                print(cart)

                Inventory.info(cart)

            elif code=="Parfait":
                Inventory.adjust_price(cart,-10)
                print("updated shopping cart")
                
                print(cart)

                Inventory.info(cart)

            input("Enter card number")
            print("Purchase done!..Enjoy your new books!")
            cart.lob.clear()




        
