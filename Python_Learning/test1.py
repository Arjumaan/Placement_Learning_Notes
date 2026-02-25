#Test Level 0,1,2!

""" 1. Bank Balance Check
Ask the user for their account balance. If balance is less than ₹1000, print "Low Balance", otherwise print "Sufficient Balance".
"""

balance = int(input("Enter your account balance: "))
if balance < 1000:
    print("Low Balance")
else:
    print("Sufficient Balance")

""" 2. Age Category
Take age as input and print:
Below 13: "Child"
13 to 19: "Teenager"
20 to 60: "Adult"
Above 60: "Senior Citizen"
"""

age = int(input("Enter your age: "))
if age < 13:
    print("Child")
elif age >= 13 and age <= 19:
    print("Teenager")
elif age >= 20 and age <= 60:
    print("Adult")
else:
    print("Senior Citizen")

""" 3. College Seat Eligibility
A college requires minimum 75% marks for admission. Take percentage as input and print "Eligible" or "Not Eligible".
"""

percentage = int(input("Enter your percentage: "))
if percentage >= 75:
    print("Eligible")
else:
    print("Not Eligible")

"""4. Simple ATM Withdrawal
Take withdrawal amount. If amount is less than or equal to available balance (₹5000), print "Withdrawal Successful", else print "Insufficient Balance".
"""

withdrawal = int(input("Enter withdrawal amount: "))
if withdrawal <= 5000:
    print("Withdrawal Successful")
else:
    print("Insufficient Balance")

"""5. Pass/Fail Checker
Take marks in 3 subjects (each out of 100). If marks in all subjects are ≥ 40, print "Pass", else print "Fail".
"""

marks1 = int(input("Enter marks in subject 1: "))
marks2 = int(input("Enter marks in subject 2: "))
marks3 = int(input("Enter marks in subject 3: "))
if marks1 >= 40 and marks2 >= 40 and marks3 >= 40:
    print("Pass")
else:
    print("Fail")

"""6. Number Sign Checker
Take a number as input and print whether it's "Positive", "Negative", or "Zero".
"""

num = int(input("Enter a number: "))
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

"""7. Even or Odd
Take a number and print if it's "Even" or "Odd".
"""

num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

"""8. Largest of Two Numbers
Take two numbers and print which one is larger (or if they're equal).
"""

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
if num1 > num2:
    print("Largest number is", num1)
elif num2 > num1:
    print("Largest number is", num2)
else:
    print("Both numbers are equal")

"""9. Marriage Eligibility
Take age and gender (M/F). For male: age ≥ 21, for female: age ≥ 18. Print "Eligible" or "Not Eligible".
"""

age = int(input("Enter your age: "))
gender = input("Enter your gender (M/F): ")
if gender == "M" or gender == "m":
    if age >= 21:
        print("Eligible")
    else:
        print("Not Eligible")
elif gender == "F" or gender == "f":
    if age >= 18:
        print("Eligible")
    else:
        print("Not Eligible")
else:
    print("Invalid gender input")

"""10. Temperature Advice
Take temperature in Celsius. If temperature > 30, print "It's hot, stay hydrated". If temperature < 15, print "It's cold, wear warm clothes". Otherwise print "Nice weather".
"""

temp = int(input("Enter temperature in Celsius: "))
if temp > 30:
    print("It's hot, stay hydrated")
elif temp < 15:
    print("It's cold, wear warm clothes")
else:
    print("Nice weather")

"""11. Simple Calculator
Take two numbers and an operator (+, -, *, /). Perform the operation and print the result.
"""

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
op = input("Enter operator (+, -, *, /): ")
if op == "+":
    print("Result:", num1 + num2)
elif op == "-":
    print("Result:", num1 - num2)
elif op == "*":
    print("Result:", num1 * num2)
elif op == "/":
    print("Result:", num1 / num2)
else:
    print("Invalid operator")

"""12. Weekday or Weekend
Take a number (1-7). Print "Weekday" for 1-5, "Weekend" for 6-7, and "Invalid" for others.
"""

day = int(input("Enter a number (1-7): "))
if day >= 1 and day <= 5:
    print("Weekday")
elif day == 6 or day == 7:
    print("Weekend")
else:
    print("Invalid")

"""13. Height Category
Take height in cm. Print:
Below 150: "Short"
150-170: "Average"
Above 170: "Tall"
"""

height = int(input("Enter your height in cm: "))
if height < 150:
    print("Short")
elif height >= 150 and height <= 170:
    print("Average")
else:
    print("Tall")

"""14. Voting Eligibility
Take age. If age ≥ 18, print "You can vote", else print "You cannot vote".
"""

age = int(input("Enter your age: "))
if age >= 18:
    print("You can vote")
else:
    print("You cannot vote")

"""15. Discount Eligibility
If purchase amount > ₹2000, give 10% discount. Print final amount after discount.
"""

amount = int(input("Enter purchase amount: "))
if amount > 2000:
    discount = amount * 0.10
    print("Discount:", discount)
    print("Final amount:", amount - discount)
else:
    print("No discount")
    print("Final amount:", amount)

"""16. Grade Based on Single Mark
Take marks out of 100. Print:
≥ 90: "A Grade"
75-89: "B Grade"
60-74: "C Grade"
40-59: "D Grade"
< 40: "F Grade"
"""

marks = int(input("Enter marks out of 100: "))
if marks >= 90:
    print("A Grade")
elif marks >= 75:
    print("B Grade")
elif marks >= 60:
    print("C Grade")
elif marks >= 40:
    print("D Grade")
else:
    print("F Grade")

"""17. Simple Interest Calculator
Take Principal, Rate, and Time. Calculate and print Simple Interest.
"""

principal = int(input("Enter Principal: "))
rate = int(input("Enter Rate: "))
time = int(input("Enter Time (in years): "))
si = (principal * rate * time) / 100
print("Simple Interest:", si)

"""18. Profit or Loss
Take Cost Price and Selling Price. Print "Profit" if SP > CP, "Loss" if CP > SP, or "No Profit No Loss" if equal.
"""

cp = int(input("Enter Cost Price: "))
sp = int(input("Enter Selling Price: "))
if sp > cp:
    print("Profit of", sp - cp)
elif cp > sp:
    print("Loss of", cp - sp)
else:
    print("No Profit No Loss")

"""19. Triangle Angle Checker
Take three angles. If their sum is 180, print "Valid Triangle", else "Invalid Triangle".
"""

a1 = int(input("Enter angle 1: "))
a2 = int(input("Enter angle 2: "))
a3 = int(input("Enter angle 3: "))
if a1 + a2 + a3 == 180:
    print("Valid Triangle")
else:
    print("Invalid Triangle")

"""20. Leap Year (Simple Rule)
Take a year. If divisible by 4, print "Leap Year", else "Not Leap Year".
"""

year = int(input("Enter a year: "))
if year % 4 == 0:
    print("Leap Year")
else:
    print("Not Leap Year")

"""21. Positive Number Check
Keep taking numbers until user enters a positive number. (Use while loop)
"""

num = int(input("Enter a number: "))
while num <= 0:
    print("Not a positive number. Try again.")
    num = int(input("Enter a number: "))
print("You entered a positive number:", num)

"""22. Simple Authentication
Set a password "python123". Ask user for password. If correct, print "Access Granted", else "Access Denied".
"""

password = "python123"
user_pass = input("Enter password: ")
if user_pass == password:
    print("Access Granted")
else:
    print("Access Denied")

"""23. Bill Splitter
Take total bill amount and number of friends. Split equally and print each person's share.
"""

bill = int(input("Enter total bill amount: "))
friends = int(input("Enter number of friends: "))
share = bill / friends
print("Each person's share:", share)

"""24. Exam Hall Allocation
Take roll number. If roll number is between 1 and 30, print "Hall A", between 31-60 print "Hall B", else "Hall C".
"""

roll = int(input("Enter roll number: "))
if roll >= 1 and roll <= 30:
    print("Hall A")
elif roll >= 31 and roll <= 60:
    print("Hall B")
else:
    print("Hall C")

"""25. Age Difference
Take age of two persons. Print who is older and by how many years.
"""

age1 = int(input("Enter age of person 1: "))
age2 = int(input("Enter age of person 2: "))
if age1 > age2:
    print("Person 1 is older by", age1 - age2, "years")
elif age2 > age1:
    print("Person 2 is older by", age2 - age1, "years")
else:
    print("Both are of the same age")

"""26. Number Comparison
Take three numbers and print the smallest number.
"""

num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))
num3 = int(input("Enter num3: "))
if num1 <= num2 and num1 <= num3:
    print("Smallest number is", num1)
elif num2 <= num1 and num2 <= num3:
    print("Smallest number is", num2)
else:
    print("Smallest number is", num3)

"""27. Simple Login System
Ask for username and password. If username is "admin" AND password is "pass123", print "Login Successful", else "Login Failed".
"""

username = input("Enter username: ")
password = input("Enter password: ")
if username == "admin" and password == "pass123":
    print("Login Successful")
else:
    print("Login Failed")

"""28. Train Ticket Price
Base price is ₹100. If age < 5, ticket is free. If age 5-12, half price. Otherwise full price. Calculate ticket price.
"""

age = int(input("Enter age: "))
base_price = 100
if age < 5:
    print("Ticket is free! Price: 0")
elif age >= 5 and age <= 12:
    print("Half price ticket:", base_price / 2)
else:
    print("Full price ticket:", base_price)

"""29. Divisibility Check
Take a number. If it's divisible by both 3 and 5, print "FizzBuzz". If only by 3, print "Fizz". If only by 5, print "Buzz". Otherwise print the number.
"""

num = int(input("Enter a number: "))
if num % 3 == 0 and num % 5 == 0:
    print("FizzBuzz")
elif num % 3 == 0:
    print("Fizz")
elif num % 5 == 0:
    print("Buzz")
else:
    print(num)

"""30. Simple Shopping Cart
Take price of 3 items. If total > ₹1000, give ₹100 discount. Print total payable amount.
"""

item1 = int(input("Enter price of item 1: "))
item2 = int(input("Enter price of item 2: "))
item3 = int(input("Enter price of item 3: "))
total = item1 + item2 + item3
if total > 1000:
    total = total - 100
    print("100 discount applied!")
print("Total payable amount:", total)



"""1. Temperature Converter
A European company needs a program that converts Celsius to Fahrenheit. Write a program that takes temperature in Celsius as input and prints the Fahrenheit equivalent.
Formula: Fahrenheit = (Celsius * 9/5) + 32
"""

celsius = int(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print("Temperature in Fahrenheit:", fahrenheit)

"""2. E-commerce Discount Calculator
An e-commerce platform offers a 10% discount if the purchase amount is above ₹1000. Write a program to calculate the final payable amount.
"""

amount = int(input("Enter purchase amount: "))
if amount > 1000:
    discount = amount * 0.10
    print("Discount:", discount)
    print("Final payable amount:", amount - discount)
else:
    print("No discount")
    print("Final payable amount:", amount)

"""3. Age Verification for Gaming
An online game needs to verify if a user is eligible (age ≥ 18). Take age as input and print "Eligible to play" or "Not eligible".
"""

age = int(input("Enter your age: "))
if age >= 18:
    print("Eligible to play")
else:
    print("Not eligible")

"""4. Simple Interest Calculator
A bank wants to calculate simple interest. Take principal, rate, and time as input and print the interest.
Formula: (P × R × T)/100
"""

p = int(input("Enter Principal: "))
r = int(input("Enter Rate: "))
t = int(input("Enter Time: "))
si = (p * r * t) / 100
print("Simple Interest:", si)

"""5. Even/Odd Number Checker
In a lottery system, tickets with even numbers get a bonus. Write a program to check if a ticket number is even or odd.
"""

ticket = int(input("Enter ticket number: "))
if ticket % 2 == 0:
    print("Even ticket - You get a bonus!")
else:
    print("Odd ticket - No bonus")

"""6. Password Validator (Basic)
A website requires passwords to be at least 8 characters long. Check if the entered password meets this criteria.
"""

password = input("Enter a password: ")
if len(password) >= 8:
    print("Password accepted")
else:
    print("Password too short! Must be at least 8 characters.")

"""7. BMI Calculator
A health app calculates BMI. Take weight (kg) and height (m) as input and print BMI.
Formula: weight / (height × height)
"""

weight = int(input("Enter weight in kg: "))
height = float(input("Enter height in meters: "))
bmi = weight / (height * height)
print("Your BMI is:", bmi)
if bmi < 18.5:
    print("Underweight")
elif bmi >= 18.5 and bmi < 25:
    print("Normal weight")
elif bmi >= 25 and bmi < 30:
    print("Overweight")
else:
    print("Obese")

"""8. Vowel/Consonant Checker
A word game needs to identify if a letter is a vowel or consonant. Take a single character as input and determine it.
"""

char = input("Enter a single character: ")
if char == "a" or char == "e" or char == "i" or char == "o" or char == "u" or char == "A" or char == "E" or char == "I" or char == "O" or char == "U":
    print(char, "is a Vowel")
else:
    print(char, "is a Consonant")

"""9. Grading System
A school grading system: marks ≥ 90 = 'A', ≥ 75 = 'B', ≥ 60 = 'C', ≥ 40 = 'D', < 40 = 'F'. Print the grade.
"""

marks = int(input("Enter marks: "))
if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
elif marks >= 40:
    print("Grade D")
else:
    print("Grade F")

"""10. Leap Year Checker
A calendar application needs to identify leap years. Take a year as input and print if it's a leap year or not.
"""

year = int(input("Enter a year: "))
if year % 400 == 0:
    print(year, "is a Leap Year")
elif year % 100 == 0:
    print(year, "is Not a Leap Year")
elif year % 4 == 0:
    print(year, "is a Leap Year")
else:
    print(year, "is Not a Leap Year")

"""11. Triangle Type Checker
A geometry app takes three sides of a triangle and determines if it's equilateral, isosceles, or scalene.
"""

s1 = int(input("Enter side 1: "))
s2 = int(input("Enter side 2: "))
s3 = int(input("Enter side 3: "))
if s1 == s2 and s2 == s3:
    print("Equilateral Triangle")
elif s1 == s2 or s2 == s3 or s1 == s3:
    print("Isosceles Triangle")
else:
    print("Scalene Triangle")

"""12. Maximum of Three Numbers
In a gaming leaderboard, find the highest score among three players. Take three scores and print the maximum.
"""

score1 = int(input("Enter score of player 1: "))
score2 = int(input("Enter score of player 2: "))
score3 = int(input("Enter score of player 3: "))
if score1 >= score2 and score1 >= score3:
    print("Highest score:", score1)
elif score2 >= score1 and score2 >= score3:
    print("Highest score:", score2)
else:
    print("Highest score:", score3)

"""13. Character Type Identifier
Take a single character as input and determine if it's a digit, alphabet, or special character.
"""

char = input("Enter a single character: ")
if char >= "0" and char <= "9":
    print("It's a Digit")
elif (char >= "a" and char <= "z") or (char >= "A" and char <= "Z"):
    print("It's an Alphabet")
else:
    print("It's a Special Character")

"""14. Electricity Bill Calculator
Calculate electricity bill: first 100 units @ ₹5/unit, next 200 units @ ₹7/unit, above @ ₹10/unit. Take units and print bill amount.
"""

units = int(input("Enter units consumed: "))
if units <= 100:
    bill = units * 5
elif units <= 300:
    bill = (100 * 5) + ((units - 100) * 7)
else:
    bill = (100 * 5) + (200 * 7) + ((units - 300) * 10)
print("Electricity Bill:", bill)

"""15. Day Name Printer
Take a number (1-7) and print the corresponding day name (1 = Monday, etc.). Print "Invalid" for other numbers.
"""

day = int(input("Enter a number (1-7): "))
if day == 1:
    print("Monday")
elif day == 2:
    print("Tuesday")
elif day == 3:
    print("Wednesday")
elif day == 4:
    print("Thursday")
elif day == 5:
    print("Friday")
elif day == 6:
    print("Saturday")
elif day == 7:
    print("Sunday")
else:
    print("Invalid")

"""16. ATM Withdrawal System
Simulate an ATM withdrawal. Take withdrawal amount and account balance. Check:
	Amount should be multiple of 100
	Sufficient balance (minimum balance ₹500 to maintain)
	Print updated balance or error message
"""

balance = int(input("Enter account balance: "))
amount = int(input("Enter withdrawal amount: "))
if amount % 100 != 0:
    print("Amount must be a multiple of 100")
elif amount > (balance - 500):
    print("Insufficient balance. Minimum balance of 500 must be maintained.")
else:
    balance = balance - amount
    print("Withdrawal successful!")
    print("Updated balance:", balance)

"""17. Tax Calculator
Income tax calculation for a company:
	Income ≤ ₹2,50,000: No tax
	₹2,50,001 - ₹5,00,000: 5%
	₹5,00,001 - ₹10,00,000: 20%
	Above ₹10,00,000: 30%
Calculate tax amount.
"""

income = int(input("Enter annual income: "))
if income <= 250000:
    tax = 0
elif income <= 500000:
    tax = (income - 250000) * 0.05
elif income <= 1000000:
    tax = (250000 * 0.05) + (income - 500000) * 0.20
else:
    tax = (250000 * 0.05) + (500000 * 0.20) + (income - 1000000) * 0.30
print("Tax amount:", tax)

"""18. Ticket Pricing System
A movie theater charges:
	Children (<12 years): ₹100
	Adults (12-60 years): ₹250
	Seniors (>60 years): ₹150
Take age and time (matinee/evening) - matinee (before 5 PM) gives 20% discount. Calculate ticket price.
"""

age = int(input("Enter age: "))
show = input("Enter show type (matinee/evening): ")
if age < 12:
    price = 100
elif age >= 12 and age <= 60:
    price = 250
else:
    price = 150
if show == "matinee":
    price = price - (price * 0.20)
    print("Matinee discount applied!")
print("Ticket price:", price)

"""19. Triangle Validity and Type
Take three angles of a triangle and check:
	If they form a valid triangle (sum = 180)
	If valid, determine if it's acute, right, or obtuse
"""

a1 = int(input("Enter angle 1: "))
a2 = int(input("Enter angle 2: "))
a3 = int(input("Enter angle 3: "))
if a1 + a2 + a3 == 180:
    print("Valid Triangle")
    if a1 == 90 or a2 == 90 or a3 == 90:
        print("Right-angled Triangle")
    elif a1 > 90 or a2 > 90 or a3 > 90:
        print("Obtuse Triangle")
    else:
        print("Acute Triangle")
else:
    print("Invalid Triangle")

"""20. Quadratic Equation Solver
Take coefficients a, b, c of quadratic equation ax² + bx + c = 0. Calculate and print the roots based on discriminant.
"""

import math
a = int(input("Enter coefficient a: "))
b = int(input("Enter coefficient b: "))
c = int(input("Enter coefficient c: "))
d = (b * b) - (4 * a * c)
if d > 0:
    root1 = (-b + math.sqrt(d)) / (2 * a)
    root2 = (-b - math.sqrt(d)) / (2 * a)
    print("Two real roots:", root1, "and", root2)
elif d == 0:
    root = -b / (2 * a)
    print("One real root:", root)
else:
    real = -b / (2 * a)
    imag = math.sqrt(abs(d)) / (2 * a)
    print("Complex roots:", real, "+", imag, "i and", real, "-", imag, "i")

"""21. Zodiac Sign Finder
Take birth date and month (as numbers) and print the zodiac sign. Handle invalid dates.
"""

day = int(input("Enter birth day: "))
month = int(input("Enter birth month (1-12): "))
if month < 1 or month > 12 or day < 1 or day > 31:
    print("Invalid date")
elif (month == 3 and day >= 21) or (month == 4 and day <= 19):
    print("Aries")
elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
    print("Taurus")
elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
    print("Gemini")
elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
    print("Cancer")
elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
    print("Leo")
elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
    print("Virgo")
elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
    print("Libra")
elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
    print("Scorpio")
elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
    print("Sagittarius")
elif (month == 12 and day >= 22) or (month == 1 and day <= 19):
    print("Capricorn")
elif (month == 1 and day >= 20) or (month == 2 and day <= 18):
    print("Aquarius")
elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
    print("Pisces")

"""22. Shipping Cost Calculator
An e-commerce site charges shipping based on weight:
	Weight ≤ 1 kg: ₹50
	1-5 kg: ₹100
	5-10 kg: ₹200
	10 kg: ₹300 + ₹20 per extra kg
Also apply 10% discount if order value > ₹2000. 
Calculate total cost.
"""

weight = int(input("Enter package weight (kg): "))
order_value = int(input("Enter order value: "))
if weight <= 1:
    shipping = 50
elif weight <= 5:
    shipping = 100
elif weight <= 10:
    shipping = 200
else:
    shipping = 300 + (weight - 10) * 20
total = order_value + shipping
if order_value > 2000:
    discount = total * 0.10
    total = total - discount
    print("10% discount applied! Discount:", discount)
print("Shipping cost:", shipping)
print("Total cost:", total)

"""23. Digital Root Calculator
Take a number and find its digital root (repeated sum of digits until single digit). Example: 987 → 9+8+7=24 → 2+4=6
"""

num = int(input("Enter a number: "))
original = num
while num >= 10:
    sum = 0
    while num > 0:
        sum = sum + num % 10
        num = num // 10
    num = sum
print("Digital root of", original, "is", num)

"""24. Traffic Light System
Simulate a traffic light. Take input as "red", "yellow", or "green" and print the appropriate message:
	Red: "Stop"
	Yellow: "Get Ready"
	Green: "Go"
Also handle invalid input.
"""

signal = input("Enter traffic light color (red/yellow/green): ")
if signal == "red":
    print("Stop")
elif signal == "yellow":
    print("Get Ready")
elif signal == "green":
    print("Go")
else:
    print("Invalid input! Please enter red, yellow, or green.")

"""25. Number to Words (1-999)
Convert a number (1-999) to words. Example: 123 → "One Hundred Twenty Three"
"""

ones = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine",
        "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen",
        "Seventeen", "Eighteen", "Nineteen"]
tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]

num = int(input("Enter a number (1-999): "))
if num < 1 or num > 999:
    print("Invalid! Enter a number between 1 and 999.")
else:
    result = ""
    if num >= 100:
        result = result + ones[num // 100] + " Hundred "
        num = num % 100
    if num >= 20:
        result = result + tens[num // 10] + " "
        num = num % 10
    if num > 0:
        result = result + ones[num]
    print("In words:", result)

"""26. Student Grade with Remarks
Take marks in 5 subjects, calculate percentage, and provide:
Grade (A/B/C/D/F)
Remarks: "Excellent" if all subjects ≥ 90, 
"Good" if average ≥ 75,
 "Needs Improvement" if any subject < 40
"""

m1 = int(input("Enter marks for subject 1: "))
m2 = int(input("Enter marks for subject 2: "))
m3 = int(input("Enter marks for subject 3: "))
m4 = int(input("Enter marks for subject 4: "))
m5 = int(input("Enter marks for subject 5: "))
total = m1 + m2 + m3 + m4 + m5
percentage = total / 5
print("Percentage:", percentage, "%")

if percentage >= 90:
    print("Grade A")
elif percentage >= 75:
    print("Grade B")
elif percentage >= 60:
    print("Grade C")
elif percentage >= 40:
    print("Grade D")
else:
    print("Grade F")

if m1 >= 90 and m2 >= 90 and m3 >= 90 and m4 >= 90 and m5 >= 90:
    print("Remarks: Excellent")
elif percentage >= 75:
    print("Remarks: Good")
if m1 < 40 or m2 < 40 or m3 < 40 or m4 < 40 or m5 < 40:
    print("Remarks: Needs Improvement")

"""27. URL Protocol Checker
Take a URL as input and check if it starts with "http://", "https://", or "ftp://". Print the protocol type or "Unknown protocol".
"""

url = input("Enter a URL: ")
if url[0:8] == "https://":
    print("Protocol: HTTPS")
elif url[0:7] == "http://":
    print("Protocol: HTTP")
elif url[0:6] == "ftp://":
    print("Protocol: FTP")
else:
    print("Unknown protocol")

"""28. Palindrome Checker (Numbers)
A puzzle game needs to check if a number is palindrome (reads same forwards and backwards). Take a number and print result.
"""

num = int(input("Enter a number: "))
temp = num
reverse = 0
while temp > 0:
    digit = temp % 10
    reverse = reverse * 10 + digit
    temp = temp // 10
if num == reverse:
    print(num, "is a Palindrome")
else:
    print(num, "is Not a Palindrome")

"""29. Working Days Calculator
Take a day number (1-7) and a boolean for holiday. Print if it's a working day:
	Monday-Friday: Working (unless holiday)
	Saturday-Sunday: Holiday (always)
"""

day = int(input("Enter day number (1=Monday, 7=Sunday): "))
holiday = input("Is it a public holiday? (yes/no): ")
if day < 1 or day > 7:
    print("Invalid day number")
elif day == 6 or day == 7:
    print("It's the weekend - Holiday!")
elif holiday == "yes":
    print("It's a public holiday - No work today!")
else:
    print("It's a working day")

"""30. EMI Calculator
Calculate monthly EMI for a loan:
EMI = P × r × (1 + r)^n / ((1 + r)^n - 1)
Where P = Principal, r = monthly interest rate, n = months. Take loan amount, annual interest rate, and years as input.
"""

p = int(input("Enter loan amount (Principal): "))
annual_rate = float(input("Enter annual interest rate (%): "))
years = int(input("Enter loan tenure (years): "))
r = annual_rate / (12 * 100)
n = years * 12
if r == 0:
    emi = p / n
else:
    emi = p * r * (1 + r)**n / ((1 + r)**n - 1)
print("Monthly EMI:", emi)
print("Total amount payable:", emi * n)
print("Total interest:", (emi * n) - p)
