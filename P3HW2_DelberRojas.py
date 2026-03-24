#P3HW2.py

#3/24/2026

#P3HW2

#you are to create a program that does the following
#ask the user to enter a name of employee
#ask the user to enter the number of hours worked this week
#ask the user to enter the hourly pay rate
#Evalute if employee has worked overtime (more than 40 hours) if yes calculate the amount owed to employee for overtime hours
#the employee should recieve 1.5 times their normal payrate for any overtime hours worked 
#Calculate amount employee should be paid for regular hours worked
#display gross pay total amount that should be paid to employee the program is to display the following 
#employee name, pay rate number of hours worked over time hours over time pay and gross pay regular hours



name = input("Enter the name of the employee: ")
hoursWorked = float(input("Enter number of hours worked this week: "))
payRate = float(input("Enter employee hourly pay rate: "))

#calculate overtime using an if/else decision structure 

if hoursWorked > 40:
    # calculate overtime 
    overTimeHours = hoursWorked - 40
    #calculate overtime pay
    overtimePay = overTimeHours * (payRate * 1.5)
    #calcualate the salary for regular hours
    regularPay = 40 * payRate
    #calculate gross pay
    grossPay = regularPay + overtimePay
else:
    overTimeHours = 0
    overtimePay = 0
    regularPay = hoursWorked * payRate
    grossPay = regularPay
    
print("-"*20)
print(f"Employee Name: {name}")

print(f'{"Hours Worked":<15}{"Pay Rate":<12}{"Over Time":<12}{"Over Time Pay":<20}{"Regular Pay":<20}{"Gross Pay":<20}')
print("-"*100)
print(f'{hoursWorked:<15}{payRate:<12}{overTimeHours:<12}{overtimePay:<20}{regularPay:<20}{grossPay:<20}')

'''
print(f"Pay Rate: ${payRate:.2f}")
print(f"Hours Worked: {hoursWorked}")
print(f"Overtime Hours: {overTimeHours}")
print(f"Overtime Pay: ${overtimePay:.2f}")
print(f"Regular Pay: ${regularPay:.2f}")
print(f"Gross Pay: ${grossPay:.2f}")
print("-"*60)
'''