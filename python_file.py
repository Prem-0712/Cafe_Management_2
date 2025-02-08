print("\nWelcome to PYTHON RESTAURANT !!!!\n")

menu = {
    "pizza": 100,
    "pasta": 80,
    "coffee": 70,
    "burger": 90,
    "shake": 70
}

print("Here is our menu:\n")
for item, price in menu.items():
    print(f"{item.capitalize()}: ₹{price}")

total_price = 0

while True:
    order = input("\nDo you want to order anything? (yes/no): ").strip().lower()
    
    if order == "no":
        break
    elif order != "yes":
        print("Invalid input. Please enter 'yes' or 'no'.")
        continue

    item = input("What would you like to have? ").strip().lower()

    if item in menu:
        total_price += menu[item]
        print(f"{item.capitalize()} added to your order. Total: ₹{total_price}")
    else:
        print("Sorry, it's not available yet.")

print(f"\nYour final bill is ₹{total_price}" if total_price > 0 else "\nThank you! Visit again.")