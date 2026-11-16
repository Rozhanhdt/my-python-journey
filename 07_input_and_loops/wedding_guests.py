SEATS_PER_TABLE = 6
PRICE_PER_EMPTY_SEAT = 500_000

guests = int(input("How many wedding guests? "))

if guests % SEATS_PER_TABLE == 0:
    tables = guests // SEATS_PER_TABLE
    print(f"Every table will be full ({tables} tables).")
    print("Congratulations, your reservation is confirmed.")
else:
    empty_seats = SEATS_PER_TABLE - (guests % SEATS_PER_TABLE)
    cost = empty_seats * PRICE_PER_EMPTY_SEAT
    print(f"{empty_seats} seats will stay empty on the last table.")
    print(f"You must pay for those empty seats: {cost:,} toman.")
    answer = input("Are you sure? (yes/no) ")

    if answer == "yes":
        print("Your reservation is confirmed, including the empty seats.")
    else:
        print("Reservation canceled.")
