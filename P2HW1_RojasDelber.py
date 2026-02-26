#Delber 
#2/19/2026 
#P2HW1 
#You will create a program that does some basic math on numbers that are entered


print("This program calculates and displays travel expenses\n")

budget = float(input("Enter Budget: "))

destination = input("Enter your travel destination: ")

gas = float(input("How much do you think you will spend on gas? "))
accommodation = float(input("Approximately, how much will you need for accomodation/hotel? "))
food = float(input("Last, how much do you need for food? "))

print()
print("-------------Travel Expenses-------------")
print(f"{ 'Location:'.ljust(20) }{destination}")
print(f"{ 'Initial Budget:'.ljust(20) }${budget:.2f}")
print(f"{ 'Fuel:'.ljust(20) }${gas:.2f}")
print(f"{ 'Accomodation:'.ljust(20) }${accommodation:.2f}")
print(f"{ 'Food:'.ljust(20) }${food:.2f}")
print("-" * 41)
remaining_balance = budget - (gas + accommodation + food)
print()
print(f"{ 'Remaining Balance:'.ljust(20) }${remaining_balance:.2f}")
