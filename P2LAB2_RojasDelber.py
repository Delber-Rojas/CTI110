#P2LAB2 
#Rojas Delber
#3/16/2026
#For this assignment, write a program that creates a dictionary where the key and value pairs are as follows
#key    #Value
#Camaro 18.21
#prius 52.36
#ModelS 110
#Silverado 26


#(notes for myself) they keys represent an automobile and the values represent the miles per gallon for each automobile.
#(after creating the dictionary, create a variable that holds all the keys in the dicitionary using the code below remember that my_dict will need to be replaced with the variable name that you assign to your dictionary.)
#My dict to store the vehicle data
vehicles = {
    'Camaro': 18.21,
    'Prius': 52.36,
    'Model S': 110.0,
    'Silverado': 26.0
}

#displaying the currently available vehicles to the user
print("dict_keys(['Camaro', 'Prius', 'Model S', 'Silverado'])")
print("Enter a vehicle to see it's mpg:", list(vehicles.keys()))

#getting the user input for the vehicle choice
vehicle_choice = input("Enter a vehicle name: ")

#check if vehicle exist and display output
if vehicle_choice in vehicles:
    mpg = vehicles[vehicle_choice]
    print(f"The {vehicle_choice} gets {mpg} mpg.")

    #how many will i drive or u drive the vehicle 
    miles = float(input(f"How many miles will you drive the {vehicle_choice}? "))

    #Calculate the gas needed
    gallons_needed = miles /mpg 
    print(f"{gallons_needed:.2f} gallons of gas are needed to drive the {vehicle_choice} {miles:.0f} miles."
    )
else:
    print("end)")



