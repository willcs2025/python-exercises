menu = {"pizza": 3.00,
         "nachos": 4.50,
         "popcorn": 6.00,
         "fries": 2.50,
         "chips": 1.00,
         "pretzel": 3.50,
         "soda": 3.00,
         "lemonade": 4.25}
cart = []
total = 0

print("--------- MENU ---------")
for key, value in menu.items():
    print(f"{key.title()}: ${value:.2f}")
print("------------------------") 


while True:
    food = input("Select an item from the menu (or type 'done' to finish): ").lower()
    if food == 'done':
        break
 elif menu.get(food) is not None:
        cart.append(food)
        total += menu[food]
        print(f"{food.title()} added to cart. Current total: ${total:.2f}")

