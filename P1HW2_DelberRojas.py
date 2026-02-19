#Delber 
#2/19/2026 
#P1HW2
#You will create a program that does some basic math on numbers that are entered


#psuedocode
#3. Ask user to enter their budget

#4. Ask user to enter travel destination

#5. Ask user for amount they will spend on gas

#6. Ask user for amount they will spend on accommodation

#7. Ask user for amount they will spend on food

#8. Add expenses

#9. Subtract expenses from budget

#10. Display results

print("This program calculates and displays travel expenses")

budget = float(input("Enter your budget:"))


destination = input("Enter your travel destination: ")


gas = float(input("How much do you think you will spend on gas: $"))
accommodation = float(input("Approximately, how much will you need for accomadation/hotel?: $"))
food = float(input("last, how much do you need for food: $"))

print("--------- Travel Expenses ---------")



total_expenses = gas + accommodation + food


remaining_budget = budget - total_expenses

print(f"Destination: {destination}")
print(f"Original Budget: ${budget:.2f}")
print(f"\nExpenses:")
print(f"  Gas: ${gas:.2f}")
print(f"  Accommodation: ${accommodation:.2f}")
print(f"  Food: ${food:.2f}")
print(f"  Total Expenses: ${total_expenses:.2f}")
print(f"\nRemaining Budget: ${remaining_budget:.2f}")

if remaining_budget >= 0:
    print(f"You have ${remaining_budget:.2f} left to spend!")
else:
    print(f"You are over budget by ${abs(remaining_budget):.2f}")


