import random

# Simple self-checkout change calculator

def disperse_change(change_amount):
    # Convert change to cents so we can count bills and coins exactly
    change_cents = round(change_amount * 100)

    dollars = change_cents // 100
    remaining_cents = change_cents % 100

    quarters = remaining_cents // 25
    remaining_cents = remaining_cents % 25

    pennies = remaining_cents

    print(f"{dollars} Dollars")
    print(f"{quarters} Quarters")
    print(f"{pennies} Pennies")


def main():
    amount_owed = round(random.uniform(1.0, 100.0), 2)

    print(f"You owe ${amount_owed:.2f}")
    cash_given = float(input("How much cash will you put in the self-checkout? "))

    change = cash_given - amount_owed
    print(f"Change is: ${change:.2f}\n")

    disperse_change(change)


if __name__ == "__main__":
    main()
