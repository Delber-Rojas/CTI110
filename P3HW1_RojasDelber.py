#P3HW1
#Delber ROjas
#You are given a partial program with bugs you are to correct the program and complete it 

#debugging the code and finishing the code 
mod_1 = float(input("Enter Grade for module 1: "))
mod_2 = float(input("Enter Grade for module 2: "))
mod_3 = float(input("Enter Grade for module 3: "))
mod_4 = float(input("Enter Grade for module 4: "))
mod_5 = float(input("Enter Grade for module 5: "))
mod_6 = float(input("Enter Grade for module 6: "))

grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]

low= min(grades)
high = max(grades)
total = sum(grades)
average = total / len(grades)

if average >= 90:
    print('Your grade is : A')
elif average >= 80:
    print('Your grade is : B')
elif average >= 70:
    print('Your grade is : C')
elif average >= 60:
    print('Your grade is : D')
else:
    print('Your grade is : F')