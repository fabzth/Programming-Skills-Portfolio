"""
Created on Wed Nov 20 20:02:49 2024

@author: fabiola patero
"""
#ASSESSMENT 2 PROGRAMMING
main_menu = ["Drinks","Hot Drinks", "Chips"]
drinks_dict = {
    2: {'name': 'Arwa Water', 'price': 0.95},
    22:{'name': 'Mai Dubai Water', 'price': 1.00},
    1:{'name': 'Sprite', 'price': 2.50},
    12:{'name': 'Pepsi', 'price': 4.00},
    13:{'name': 'Sprite', 'price': 4.75},
    14:{'name': 'Coke Zero', 'price': 3.50}
    }
hotdrinks_dict = {
    1: {'name': 'Cappuccino', 'price': 4.00},
    12: {'name': 'Espresso', 'price': 4.00},
    2: {'name': 'Hot Chocolate', 'price': 3.75},
    13: {'name': 'Americano', 'price': 5.00},
    14: {'name': 'Mochaccino', 'price': 5.95},
    22: {'name': 'Cocoa', 'price': 5.00}
}
chips_dict = {
    1: {'name': 'Cheese Cheetos', 'price': 3.50},
    12: {'name': 'Flaming Hot Cheetos', 'price': 3.00},
    2: {'name': 'Tomato ketchup Lay’s Chips', 'price': 5.00},
    22: {'name': 'Vinegar Lay’s Chips', 'price': 5.00},
    3: {'name': 'Cheese Lay’s Chips', 'price': 2.50},
    32: {'name': 'Original Pringles', 'price': 4.00}
    }
addons_dict= {
    1: {'name': 'Hershey’s Chocolate', 'price': 3.00},
    12: {'name': 'M&m’s Minis', 'price': 2.50},
    13: {'name': 'M&m’s Peanut', 'price': 2.75},
    14: {'name': 'Bueno Chocolate', 'price': 3.40},
    21: {'name': 'Monster Energy Drink', 'price': 6.00},
    31: {'name': 'Mentos Fresh Breathe', 'price': 3.10}
}
total = 0

def main_menu_func():
    print(main_menu)
    x = str(input("\n\n·.★·.·´¯`·.·★ PLEASE CHOOSE THE CATEGORY YOU WANT. ★·.·´¯`·.·★.·. Type EXIT to finish.\n\n")).capitalize()
    if x == 'Drinks': #using the if condition when the consumer chose drinks
        drinks_func()
    if x== 'Hot Drinks': #using the if condition when the consumer chose hot drinks
        hotdrinks_func()
    elif x == 'Chips': #using the if condition when the consumer chose chips
        chips_func()
    else:
        print("\n\n°•.•°¤*✬.•°°• NOW YOU CAN PICK UP YOUR ITEMS.✬ DON'T FORGET YOUR CHANGE:3 °•°•.✬*¤°•.•°\n")
        change_func() #this will print the receipt once the purchase is done

def another_drink():
    x = input("\n\n¯`’•.♥ ♥WOULD YOU CARE FOR ANOTHER DRINK ?(¯`’•.¸❤♫♪♥(◠‿◠)♥♫♪❤¸.•’´¯) Type YES or NO:\n").upper()
    if x == 'YES': #using the if condition to ask the buyer for another purchase
        drinks_func()
    else:
        main_menu_func() #will return to main menu

def another_hotdrink():
    x = input("\n\n★¸.•☆•.¸★ WOULD YOU CARE FOR ANOTHER HOT DRINK ? ★⡀.•☆•.★ Type YES or NO:\n").upper()
    if x == 'YES': 
        hotdrinks_func() #using the if condition to ask the buyer for another purchase
    else:
        main_menu_func() #will return to main menu

def another_chips():
    x = input("\n\nミ★ WOULD YOU LIKE TO GET ANOTHER CHIPS ? ★彡 Type YES or NO:\n").upper()
    if x == 'YES': 
        chips_func()
    else:
        main_menu_func() 

def add_ons_func():
    global total
    print(addons_dict)
    print("\n\nTYPE IN THE ADD-ON YOU WANT. IF YOU DON'T WANT ANYMORE ADD-ON, type SKIP.\n") 
    addon_input = input()  #Reading this input as a string
    if addon_input.upper() == 'SKIP': #using uppercase method to compare as string
        main_menu_func()
    else:
        addon_id = int(addon_input) #this is to convert to an integer, else 'EXIT'
        if addon_id in addons_dict:
            addon_cost = addons_dict[addon_id]['price']
            total += addon_cost
            main_menu_func()
        else:
            print("\n\nUH OH! ENTER A VALID ADD-ON.\n")
            add_ons_func()

def drinks_func():
    global total
    print(drinks_dict)
    print("\n\n°⨳°·..·°⨳°⊹٭ PLEASE TYPE IN THE DRINK YOU WANT ٭⊹°⨳°·..·°⨳°. IF YOU DON'T WANT ANYMORE DRINK, type SKIP:\n") 
    drink_input = input() #Reading this input as a string
    if drink_input.upper() == 'SKIP': #using uppercase method to compare as string
        main_menu_func()
    else:
        drink_id = int(drink_input)  #this is to convert to an integer, else 'EXIT'
        if drink_id in drinks_dict:
            drink_cost = drinks_dict[drink_id]['price']
            total += drink_cost
            add_ons_func() 
        else:
            print("\n\nOH NO! PLEASE ENTER A VALID DRINK.\n\n")
            drinks_func()

def hotdrinks_func():
    global total
    print(hotdrinks_dict)
    print("\n\n°⨳°·..·°⨳°⊹٭ PLEASE TYPE IN THE HOT DRINK YOU WANT ٭⊹°⨳°·..·°⨳°. IF YOU DON'T WANT ANYMORE DRINK, type SKIP:\n") 
    hotdrink_input = input() 
    if hotdrink_input.upper() == 'SKIP': 
        main_menu_func()
    else:
        hotdrink_id = int(hotdrink_input)  
        if hotdrink_id in hotdrinks_dict:
            hotdrink_cost = hotdrinks_dict[hotdrink_id]['price']
            total += hotdrink_cost #using the assignment orperator to total the cost of the hot drink
            add_ons_func() 
        else:
            print("\n\nOH NO! PLEASE ENTER A VALID DRINK.\n\n")
            hotdrinks_func() #the loop will continue to print until the input is accurate
            
def chips_func():
    global total
    print(chips_dict)
    print("\n\n•¤»((¯♥¯))«¤• PLEASE TYPE IN THE CHIPS YOU WANT •¤»((¯♥¯))«¤•:\n") 
    chips_id = int(input()) 
    if chips_id in chips_dict:
        chips_cost = chips_dict[chips_id] ['price']
        total += chips_cost 
        add_ons_func()
    else:
        print("\n\nOOPS ! ENTER A VALID CHIPS OPTION.\n\n")
        chips_func() 

def change_func():
    global total
    print("\n\n❤꧁ღ⊱♥ THANK YOU FOR BUYING FROM ZETH'S VENDING MACHINE COLLECTION. WE HOPE TO SEE YOU AGAIN ! ♥⊱ღ꧂❤")
    change = coins - total  #using arithmetic operations to deduct the sum from the coins for the change
    print("\nYOU PAID", coins, "WITH", str(total), ". AND YOUR CHANGE WILL BE:", change)

print('٭⊹°⨳°·..·°⨳° ((¯♥¯))WELCOME TO ZETHS VENDING MACHINE COLLECTION! ((¯♥¯)) ٭⊹°⨳°·..·°⨳°')
coins = float(input('\n°•.•°¤*✬.•°°• Please enter your coins down here: °•°•.✬*¤°•.•°\n '))

coin_type = str(input('\n\nAre your coins DIRHAMS ? Please type YES or NO:\n'))
if coin_type == "YES": #when true, continue with the next print
    print("\nYOU HAVE ENTERED", str(coins), "DHS. SELECT THE CATEGORY YOU LIKE\n")
    print(main_menu)
    print("\n\nTYPE THE CATEGORY YOU WANT:\n")
    category_selection = str(input()).capitalize() #To pick between beverages, hot drinks, and chips on the main menu
    if category_selection == 'Drinks':
        drinks_func()
    if category_selection == 'Hot Drinks':
        hotdrinks_func()
    elif category_selection == 'Chips':
        chips_func() #using the if-elif condition for the main menu
    else:
        print("OOPS ! try again.") # the loop will break whenever there is an error in the input
else:
    print('\*¸ „„.•~¹°”ˆ˜¨♡ Sorry, but we only accept DIRHAMS. TRY AGAIN!:3 ♡¨˜ˆ”°¹~•.„¸*') # the loop will break whenever there is an error in the input.