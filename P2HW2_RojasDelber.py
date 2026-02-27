#Delber Rojas 
#2/26/2026
#P2HW2 
#This assignemnt is to assess student understandings of lists, loops, and functions.


#this python assignment will ask the users to enter grades for the following test each grade it to be requestesd in a seperate statement
#display the follwing
#the lowest grade
#the highest grade
#sum of grades
#The grades average




module_grades = []
print("Grade Entry System")
print("-----------------------------------")

module_grades.append(float(input("Enter grade for Module 1: ")))
module_grades.append(float(input("Enter grade for Module 2: ")))
module_grades.append(float(input("Enter grade for Module 3: ")))
module_grades.append(float(input("Enter grade for Module 4: ")))
module_grades.append(float(input("Enter grade for Module 5: ")))
module_grades.append(float(input("Enter grade for Module 6: ")))


print("-----------------------------------")
print("Grade Statistics")
print("-----------------------------------")

lowest_grade = min(module_grades)
print(f"Lowest Grade: {lowest_grade}")


highest_grade = max(module_grades)
print(f"Highest Grade: {highest_grade}")


sum_grades = sum(module_grades)
print(f"Sum of Grades: {sum_grades}")

average_grade = sum_grades / len(module_grades)
print(f"Average Grade: {average_grade:.2f}")

print("-----------------------------------")
