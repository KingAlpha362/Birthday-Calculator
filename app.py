from datetime import datetime # import the datetime module

now = datetime.now() # get the current date and time
current_year, current_month = now.year, now.month # get the current month and year

name = input("What is your name? ") # ask the user for their name
age = int(input(f"How old are you {name}? ")) # ask the user for their age
birth_month = int(input(f"Which month were you born in {name} (1-12)? ")) #
birth_year = int(input(f"Which year were you were born in {name} ? ")) # ask the user for their birth year

calculated_age = current_year - birth_year - (birth_month > current_month) # calculate the user's age

# check if the calculated age is the same as the age the user provided
if calculated_age == age:
    print(f"Hello {name}! You are {age} years old and your birth year is {birth_year}.")
else: 
    print(f"Based on your birth month you are actually {calculated_age} years old.")
exit()

# Check if the user is an adult or a minor
if age >= 20:
    print("You are an adult")
else:
    print("You are still a minor")
exit()

age = int(input("How old are you? ")) # ask the user for their age

days_alive = age * 365 # calculate the number of days the user has been alive
hours_alive = days_alive * 24 # calculate the number of hours the user has been alive
minutes_alive = hours_alive * 60 # calculate the number of minutes the user has been alive
seconds_alive = minutes_alive * 60 # calculate the number of seconds the user has been alive
weeks_alive = days_alive / 7 # calculate the number of weeks the user has been alive
months_alive = age * 12 # calculate the number of months the user has been alive

print(f"You have been alive for {days_alive} days.")
print(f"You have been alive for {hours_alive} hours.")
print(f"You have been alive for {minutes_alive} minutes.")
print(f"You have been alive for {seconds_alive} seconds.")
print(f"You have been alive for {weeks_alive} weeks.")
print(f"You have been alive for {months_alive} months.")
exit

num_1 = int(input("Enter the first number: "))
num_2 = int(input("Enter the second number: "))

ans = num_1 + num_2

print(f"The sum of {num_1} and {num_2} is {ans}")	
exit()

# Calculate the user's gross pay, deductions and net pay
hours = float(input("Enter the number of hours you worked: "))
hourly_rate = float(input("Enter your hourly rate: "))

total_days_in_month = 30
weekends_per_month = 8

# Calculate the number of working days in the month
working_days = total_days_in_month - weekends_per_month 

# Calculate the gross pay, deductions and net pay
gross = hours * hourly_rate * working_days

deductions = gross * 0.2

netpay = gross - deductions

print(f"Number of working days in the month: {working_days}")
print(f"Your gross pay is: ZAR {gross:.2f}")
print(f"Your deductions (20%) are: ZAR {deductions:.2f}")
print(f"Your net pay is: ZAR {netpay:.2f}")
exit()

# Check if the user has passed or failed based on their score and code
student_score = int(input("Enter your score: "))

score = int(student_score)

if 80 <= score <= 100:
    print("code: 7")
elif 70 <= score <= 79:
    print("code: 6")
elif 60 <= score <= 69:
    print("code: 5")
elif 50 <= score <= 59:
    print("code: 4")
elif 40 <= score <= 49:
    print("code: 3")
elif 30 <= score <= 39:
    print("code: 2")
elif 0 <= score <= 29:
    print("code: 1")
else:
    print("Invalid score")
exit()
      