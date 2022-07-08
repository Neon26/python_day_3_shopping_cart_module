#1) Build a Shopping Cart
#You can use either lists or dictionaries. The program should have the following capabilities:

#1) Takes in input
#2) Stores user input into a dictionary or list
#3) The User can add or delete items
#4) The User can see current shopping list
#5) The program Loops until user 'quits'
#6) Upon quiting the program, print out all items in the user's list

cart = {}
print()
print("Welcom to the Shopping cart Program!")

print()


def add_item():
    shopping = True
    print(" \nTo stop adding type: 'Quit'")
    while shopping:
        item = input("\nWhat would you like to add to your shopping cart?")
        item = item.lower()
        if item != 'quit':
            if item not in cart:
                cart[item] = 1
            else:
                    cart[item] += 1
        else:
                shopping = False

def view_item():
    print("The contents in your cart are: ")
    for item, quant in cart.items():
        print(f"{item.title()} [{quant}]")


def delete_item():
    deleting = True
    print(" To stop deleting type: 'Quit'")
    while deleting:
        item = input('What would you like to delete?')
        item = item.lower()
        if item == 'quit':
            deleting= False
            print('Items removed')
        else:
            if item not in cart:
                print("not in cart")
            else:
                cart[item] -=1
                if item ==0:
                    del cart[item]

def shopping_list():
    shopping = True
    while shopping:
        do = input("Please select one of the following: \n1. add \n2. view \n3. delete \n4. quit: \n ")
        if do == 'add':
            add_item()
        elif do == 'delete':
            delete_item()
        elif do == 'view':
            view_item()
        elif do ==  'quit':
            print("Thank you for shopping with us. Goodbye.")
            shopping = False


shopping_list()

        
    














