inventory = {"apple": 5, "coffee": 3, "cookie": 8, "water": 10}
prices    = {"apple": 1.50, "coffee": 3.75, "cookie": 2.00, "water": 1.00}
on_sale   = {"apple", "cookie"}

DISCOUNT    = 0.20
store_money = 0.0
#DEFINITION DOES NOT DO ANYTHINFFG
def show_menu():
    print("PYTHON STOREEEEEE")
    for item ,desc in inventory:
        p = prices[item] * (1 - DISCOUNT) if item in on_sale else prices[item]
        sale = " (SALE)" if item in on_sale else ""
        print(f"  {item:<8} ${p:.2f}  stock:{inventory[item]}{sale}")
    print(f"  Earnings: ${store_money:.2f}")
    print("Type item name to buy, or EXIT")

#ts is DEFINITION IT DOSENT DO SHYT
def buy(item):
    global store_money
    if item not in inventory:
        print("Item not found.")
        return
    if inventory[item] == 0:
        print(f"{item} is out of stock!")
        return
    p = prices[item] * (1 - DISCOUNT) if item in on_sale else prices[item]
    inventory[item] -= 1
    store_money += p
    print(f"Bought {item} for ${p:.2f}. Stock left: {inventory[item]}. Earnings: ${store_money:.2f}")
 

#ts is infinant (THIS RUNS THE CODE NOT THE FRIKING DEFINITIONS)
while True:
     show_menu()
     choice = input("type here ->").strip().lower()
     if choice == "exit":
        print("Thanks! Goodbye.")
        break
     else:
        buy(choice)
    