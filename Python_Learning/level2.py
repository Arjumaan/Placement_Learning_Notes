#-----------------------------
#Level 2 Practice Questions!
#-----------------------------

#1. Write a program to check whether a person is eligible to vote based on age.
age = int(input("Enter age: "))
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

#2. Write a program to check whether a given number is even or odd.
num = int(input("Enter number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

#3. Write a program to find the largest of two numbers. If both numbers are equal print a suitable message.
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
if num1 > num2:
    print("Largest number is", num1)
elif num2 > num1:
    print("Largest number is", num2)
else:
    print("Both numbers are equal.")

#4. Write a program to check whether a students has passed or failed based on the marks obtained. Passing mark is 40.
marks = int(input("Enter marks: "))
if marks >= 40:
    print("Pass")
else:
    print("Fail")

#5. Write a program to check whether a given number is positive, negative or zero.
num = int(input("Enter number: "))
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

#6. Write a program to calculate and display the grade of the student based on marks.
marks = int(input("Enter marks: "))
if marks >= 90:
    print("Grade A")
elif marks >= 80:
    print("Grade B")
elif marks >= 70:
    print("Grade C")
elif marks >= 60:
    print("Grade D")
else:
    print("Grade F")

#7. Write a program to perform a simple login validation using username and password.
username = input("Enter username: ")
password = input("Enter password: ")
if username == "admin" and password == "admin":
    print("Login successful")
else:
    print("Invalid credentials")

#8. Write a program to check whether a given year is a leap year or not.
year = int(input("Enter year: "))
if year % 4 == 0:
    print("Leap year")
else:
    print("Not a leap year")

#9. Write a program to calculate the discount amount based on the total shopping bill. 
discount = 0.10
bill = int(input("Enter bill amount: "))
if bill >= 1000:
    print("Discount amount is", bill * discount)
    print("Total amount is", bill - (bill * discount))
else:
    print("No discount")
    print("Total amount is", bill)

#10. Write a program to check whether an ATM withdrawal is possible based on account balance. 
min_balance = 1000
balance = int(input("Enter balance: "))
withdrawal = int(input("Enter withdrawal amount: "))
if balance >= withdrawal:
    print("Withdrawal successful")
else:
    print("Insufficient balance")

#11. Write a program to check whether a given character is a vowel or a consonant.
char = input("Enter a character: ")
if char in "aeiouAEIOU":
    print("Vowel")
else:
    print("Consonant")

#12. Write a program to accept three numbers and find the largest among them.
num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))
num3 = int(input("Enter num3: "))
if num1 >= num2 and num1 >= num3:
    print("Largest number is", num1)
elif num2 >= num1 and num2 >= num3:
    print("Largest number is", num2)
else:
    print("Largest number is", num3)

#13. Write a program to calculate electricity bill based on the following: Units <= 100 -> $2 per unit, Units 101 - 300 -> $3 per unit, Units > 300 -> $5 per unit.
units = int(input("Enter units: "))
if units <= 100:
    print("Total amount is", units * 2)
elif units <= 300:
    print("Total amount is", units * 3)
else:
    print("Total amount is", units * 5) 

#14. Write a program to check whether a given number is a valid triangle angle set (Sum of three angles = 180). 
num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))
num3 = int(input("Enter num3: "))
if num1 + num2 + num3 == 180:
    print("Valid triangle angle set")
else:
    print("Invalid triangle angle set")

#15. Write a program to calculate salary bonus: if years of experience >= 5 10% bonus, else no bonus.
experience = int(input("Enter years of experience: "))
salary = int(input("Enter salary: "))
if experience >= 5:
    print("Bonus amount is", salary * 0.10)
    print("Total amount is", salary + (salary * 0.10))
else:
    print("No bonus")
    print("Total amount is", salary)