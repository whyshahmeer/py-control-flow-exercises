# Q1. Read a number. Print Positive, Negative, or Zero.

print("Positive, Negative, or Zero\n")

number = float(input("Enter a number: "))

if number > 0:
    print("The number is Positive.")
elif number < 0:
    print("The number is Negative.")
else:
    print("The number is Zero.")

print("\n")

# Q2. Read a number. Print Even or Odd.

print("Even or Odd Checker\n")

number = int(input("Enter a number: "))

remainder = number % 2

if remainder == 0:
    print(f"{number} is an Even number.")
else:
    print(f"{number} is an Odd number.")

print("\n")

# Q3. Read your age. Print Eligible to Vote or Not Eligible.

print("Voting Eligibility Checker\n")

age = int(input("Enter your age: "))

minimum_age = 18

if age >= minimum_age:
    print("You are Eligible to Vote!")
else:
    print("You are Not Eligible to Vote!")

print("\n")

# Q4. Read two numbers. Print the bigger number.

print("Bigger Number Finder\n")

number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))

if number1 > number2:
    print(f"The bigger number is {number1}.")
elif number2 > number1:
    print(f"The bigger number is {number2}.")
else:
    print("Both numbers are equal.")

print("\n")

# Q5. Read three numbers. Print the smallest number.

print("Smallest Number Finder\n")

number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))
number3 = float(input("Enter the third number: "))

if number1 <= number2 and number1 <= number3:
    print(f"{number1} is the smallest number.")
elif number2 <= number1 and number2 <= number3:
    print(f"{number2} is the smallest number.")
else:
    print(f"{number3} is the smallest number.")

print("\n")

# Q6. Read a year and check if it is leap or not.

print("Leap Year Checker\n")

year = int(input("Enter a year: "))

if year % 400 == 0:
    result = "Leap Year"
elif year % 100 == 0:
    result = "Not a Leap Year"
elif year % 4 == 0:
    result = "Leap Year"
else:
    result = "Not a Leap Year"

print(f"{year} is a {result}.")

print("\n")

# Q7. Read a month number (1-12). Print the month name using match-case.

print("Month Name Finder\n")

month = int(input("Enter a month number (1-12): "))

match month:
    case 1:
        month = "January"
    case 2:
        month = "February"
    case 3:
        month = "March"
    case 4:
        month = "April"
    case 5:
        month = "May"
    case 6:
        month = "June"
    case 7:
        month = "July"
    case 8:
        month = "August"
    case 9:
        month = "September"
    case 10:
        month = "October"
    case 11:
        month = "November"
    case 12:
        month = "December"
    case _:
        month = "Invalid month number"

print(f"Month: {month}")

print("\n")

# Q8. Ask the user to enter two numbers. If both numbers are exactly the same,
# print "They are equal". Otherwise, print "They are different".

print("Number Comparison\n")

number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))

if number1 == number2:
    print("They are equal.")
else:
    print("They are different.")

print("\n")

# Q9. Read a traffic signal (Red, Yellow, Green).
# Print the correct action using match-case.

print("Traffic Signal\n")

traffic_signal = input("Enter the traffic signal (Red, Yellow, Green): ")

match traffic_signal:
    case "red":
        print("Stop!")
    case "yellow":
        print("Get Ready!")
    case "green":
        print("Go!")
    case _:
        print("Invalid traffic signal")

print("\n")

# Q10. Make a simple calculator.
# Read two numbers and an operator (+, -, *, /).

print("Simple Calculator\n")

number1 = float(input("Enter the first number: "))
operator = input("Enter an operator (+, -, *, /): ")
number2 = float(input("Enter the second number: "))

match operator:
    case "+":
        print(f"Result: {number1 + number2}")
    case "-":
        print(f"Result: {number1 - number2}")
    case "*":
        print(f"Result: {number1 * number2}")
    case "/":
        print(f"Result: {number1 / number2}")
    case _:
        print("Invalid operator.")

print("\n")

# Q11. Ask the student to enter their test percentage.
# Use elif to find their letter grade:
# • 90% or above → Grade A
# • 75% to 89% → Grade B
# • 50% to 74% → Grade C
# • Below 50% → Grade F

print("Student Grade Checker\n")

percentage = float(input("Enter your test percentage: "))

if percentage >= 90:
    print("Grade: A")
elif percentage >= 75:
    print("Grade: B")
elif percentage >= 50:
    print("Grade: C")
else:
    print("Grade: F")

print("\n")


# Q12. Temperature Guide
# Ask the user to enter today's temperature in Celsius.
# • If it is above 30 degrees, print "It is hot".
# • If it is between 15 and 30 degrees (inclusive), print "It is pleasant".
# • If it is below 15 degrees, print "It is cold".

print("Temperature Guide\n")

temperature = float(input("Enter today's temperature in Celsius: "))

if temperature > 30:
    print("It is hot.")
elif temperature >= 15 and temperature <= 30:
    print("It is pleasant.")
else:
    print("It is cold.")

print("\n")

# Q13. Ask the user to pick a food item by typing a letter:
# 'P' for Pizza, 'B' for Burger, or 'S' for Sandwich.
# Use match-case to display the price.

print("Food Menu\n")

food_choice = input("Enter a food letter (P, B, S): ")

match food_choice:
    case "P":
        print("Pizza Price: $10")
    case "B":
        print("Burger Price: $6")
    case "S":
        print("Sandwich Price: $4")
    case _:
        print("Item not available.")

print("\n")

# Q14. Ask the user how much money they spent at a toy store.
# • If they spent more than $100, give them a $20 discount and print the final price.
# • If they spent more than $50 but less than $100, give them a $5 discount and print the final price.
# • Otherwise, print the original price with no discount.

print("Toy Store Discount Calculator\n")

amount_spent = float(input("Enter the amount you spent: $"))

if amount_spent > 100:
    final_price = amount_spent - 20
    print("You received a $20 discount.")
    print(f"Final Price: ${final_price}")
elif amount_spent > 50:
    final_price = amount_spent - 5
    print("You received a $5 discount.")
    print(f"Final Price: ${final_price}")
else:
    print("No discount applied.")
    print(f"Final Price: ${amount_spent}")

print("\n")


# Q15. Ask the user for their age. If they are 12 years old or older,
# ask them if they are a student ("yes" or "no").
# • If they are a student, the ticket costs $8.
# • If they are not a student, the ticket costs $12.
# • If they are under 12 years old, the ticket is free.

print("Ticket Price Checker\n")

age = int(input("Enter your age: "))

if age >= 12:
    student = input("Are you a student? (yes/no): ")

    if student == "yes":
        print("Ticket Price: $8")
    else:
        print("Ticket Price: $12")
else:
    print("Your ticket is free.")

print("\n")

# Q16. Ask the applicant for two things: their age and their years of experience.
# Solve it using nested if.
# • If they are 21 or older, check their experience:
#     - If they have 3 or more years of experience, print "You are hired!".
#     - Otherwise, print "You need more experience".
# • If they are under 21, print "You are too young for this job".

print("Job Eligibility Checker\n")

age = int(input("Enter your age: "))

if age >= 20:
    experience = int(input("Enter your years of experience: "))

    if experience >= 3:
        print("You are hired!")
    else:
        print("You need more experience.")
else:
    print("You are too young for this job.")

print("\n")

# Q17. ATM: Read account balance and withdrawal amount.
# Check if money can be withdrawn.

print("ATM Withdrawal Checker\n")

account_balance = float(input("Enter your account balance: $"))
withdrawal_amount = float(input("Enter the withdrawal amount: $"))

if withdrawal_amount <= account_balance:
    remaining_balance = account_balance - withdrawal_amount

    print("Withdrawal successful.")
    print(f"Remaining Balance: ${remaining_balance}")
else:
    print("Insufficient balance!Withdrawal denied.")

print("\n")

# Q18. Bank Loan: Read age, monthly income, and job status.
# Decide if the loan is approved.

print("Bank Loan Eligibility Checker\n")

age = int(input("Enter your age: "))
monthly_income = float(input("Enter your monthly income: $"))
job_status = input("Are you employed? (yes/no): ")

if age >= 20:
    if monthly_income >= 70000:
        if job_status == "yes":
            print("Loan Approved.")
        else:
            print("Loan Rejected. You must have a job.")
    else:
        print("Loan Rejected. Monthly income is too low.")
else:
    print("Loan Rejected. You must be at least 18 years old.")

print("\n")

# Q19. Store a secret number (like 7) inside a variable.
# Ask the user to guess the number.
# • If they guess it right, print "Correct guess!".
# • If their guess is too high, print "Too high, try again!".
# • If their guess is too low, print "Too low, try again!".

print("Guess the Secret Number\n")

secret_number = 7
guess = int(input("Guess the secret number: "))

if guess == secret_number:
    print("Correct guess!")
elif guess > secret_number:
    print("Too high, try again!")
else:
    print("Too low, try again!")

print("\n")

# Q20. Ask the user for the distance (in km).
# • Less than 5km: $5 fee.
# • 5km to 15km: $10 fee.
# • More than 15km: $15 fee.

print("Delivery Fee Calculator\n")

distance = float(input("Enter the distance (in km): "))

if distance < 5:
    print("Delivery Fee: $5")
elif distance <= 15:
    print("Delivery Fee: $10")
else:
    print("Delivery Fee: $15")

print("\n")