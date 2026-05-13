#Delber Rojas
#5/6/2026
#llm_lab1

"""Simple arithmetic calculator.

This program performs addition, subtraction, multiplication, and division.
It uses a simple text menu and validates numeric input.
"""

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        print("Cannot divide by zero.")
        return None
    return a / b


def main():
    print("Simple Calculator")
    print("Choose an operation:")

    while True:
        print("\n1) Add")
        print("2) Subtract")
        print("3) Multiply")
        print("4) Divide")
        print("5) Exit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "5":
            print("Goodbye!")
            break

        if choice not in {"1", "2", "3", "4"}:
            print("Please choose a valid option.")
            continue

        x = get_number("Enter the first number: ")
        y = get_number("Enter the second number: ")

        if choice == "1":
            result = add(x, y)
            operator = "+"
        elif choice == "2":
            result = subtract(x, y)
            operator = "-"
        elif choice == "3":
            result = multiply(x, y)
            operator = "*"
        else:
            result = divide(x, y)
            operator = "/"

        if result is not None:
            print(f"{x} {operator} {y} = {result}")


if __name__ == "__main__":
    main()
