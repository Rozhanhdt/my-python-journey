sandwich_orders = [
    "tuna",
    "pastrami",
    "veggie",
    "pastrami",
    "ham",
    "pastrami",
    "turkey",
]
finished_sandwiches = []
dream_vacations = {}

print("The deli has run out of pastrami.")
while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")

while sandwich_orders:
    current = sandwich_orders.pop(0)
    print(f"I made your {current} sandwich.")
    finished_sandwiches.append(current)

print("\nSandwiches made today:")
for sandwich in finished_sandwiches:
    print(f"- {sandwich}")

print("\nFree trip poll for anyone still in line.")
polling = True
while polling:
    name = input("\nWhat is your name? ")
    place = input(
        "If you could visit one place in the world, where would you go? "
    )
    dream_vacations[name] = place

    another = input("Is another customer waiting? (yes/no) ")
    if another == "no":
        polling = False

print("\nDream vacation poll:")
for name, place in dream_vacations.items():
    print(f"{name} would go to {place}.")
