print("Welcome to Pizza Palace Cinema.")
print("Enter 'quit' whenever you want to move on.")

# while stops when the condition becomes false.
topping = ""
while topping != "quit":
    topping = input("\nPizza topping: ")
    if topping != "quit":
        print(f"I'll add {topping} to your pizza.")

# An active flag keeps the loop going until it is set to False.
active = True
while active:
    age_text = input("\nGuest age for a movie ticket: ")
    if age_text == "quit":
        active = False
    else:
        age = int(age_text)
        if age < 3:
            print("Your ticket is free.")
        elif age <= 12:
            print("Your ticket costs $10.")
        else:
            print("Your ticket costs $15.")

# break leaves the loop immediately, even though the while test is always True.
while True:
    drink = input("\nDrink to add to the order: ")
    if drink == "quit":
        break
    print(f"I'll add {drink} to your order.")

print("\nOrder saved. The neon sign stays on until you press CTRL-C.")

# This loop has no quit. Stop it with CTRL-C.
while True:
    print("Pizza Palace Cinema is open all night!")
