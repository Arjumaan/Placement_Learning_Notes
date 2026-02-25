''' 
An online shopping platform displays a personalized greeting message when a customer logs into the website.
A function is defined using the def keyword to generate the welcome message dynamically based on the username entered during login
'''

def welcome_message(username):
    return f"Welcome, {username}!"

username = input("Login username: ")
print(welcome_message(username))

#1. A shop owner wants to print a welcome message to customers. Write a program to display 'Welcome to ABC Store'.

print("Welcome to ABC Store")

#2. A teacher wants to take student name as input and greet them. Write a program.

name = input("Enter student name: ")
print("Hello", name, "! Welcome to class.")

#3. A bank collects customer age. Write a program to store age and print its datatype.

age = input("Enter your age: ")
print("Age:", age)
print("Datatype:", type(age))

age = int(age)
print("After conversion:", age)
print("Datatype:", type(age))

#4. A store calculates total bill from two item prices entered by user.

item1 = int(input("Enter price of item 1: "))
item2 = int(input("Enter price of item 2: "))
total = item1 + item2
print("Total bill:", total)

#5. Check if a number entered by user is even or odd.

num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

#6. A company gives bonus if salary > 50000. Write condition check.

salary = int(input("Enter salary: "))
if salary > 50000:
    bonus = salary * 0.10
    print("Bonus:", bonus)
    print("Total salary:", salary + bonus)
else:
    print("No bonus")
    print("Total salary:", salary)

#7. Print numbers from 1 to 5 using loop.

i = 1
while i <= 5:
    print(i)
    i = i + 1

#8. A password system checks if entered password equals 'admin123'.

password = input("Enter password: ")
if password == "admin123":
    print("Access Granted")
else:
    print("Access Denied")

#9. Count total characters in a user-entered string.

text = input("Enter a string: ")
count = len(text)
print("Total characters:", count)

#10. Reverse a string entered by user.

text = input("Enter a string: ")
reverse = ""
i = len(text) - 1
while i >= 0:
    reverse = reverse + text[i]
    i = i - 1
print("Reversed string:", reverse)

#11. Calculate square of a number using operator.

num = int(input("Enter a number: "))
square = num * num
print("Square of", num, "is", square)

#12. Check if a person is eligible to vote (age >= 18).

age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")

#13. Print multiplication table of a number.

num = int(input("Enter a number: "))
i = 1
while i <= 10:
    print(num, "x", i, "=", num * i)
    i = i + 1

#14. Check if a string contains the word 'Python'.

text = input("Enter a string: ")
if "Python" in text:
    print("Yes, it contains 'Python'")
else:
    print("No, it does not contain 'Python'")

#15. Find largest of two numbers.

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
if num1 > num2:
    print("Largest number is", num1)
elif num2 > num1:
    print("Largest number is", num2)
else:
    print("Both numbers are equal")

#16. Print numbers from 10 to 1 using while loop.

i = 10
while i >= 1:
    print(i)
    i = i - 1

#17. Convert temperature from Celsius to Fahrenheit.

celsius = int(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print("Temperature in Fahrenheit:", fahrenheit)

#18. Count vowels in a string.

text = input("Enter a string: ")
count = 0
i = 0
while i < len(text):
    if text[i] == "a" or text[i] == "e" or text[i] == "i" or text[i] == "o" or text[i] == "u":
        count = count + 1
    if text[i] == "A" or text[i] == "E" or text[i] == "I" or text[i] == "O" or text[i] == "U":
        count = count + 1
    i = i + 1
print("Total vowels:", count)

#19. Check if number is positive, negative or zero.

num = int(input("Enter a number: "))
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

#20. Calculate simple interest.

p = int(input("Enter principal: "))
r = int(input("Enter rate: "))
t = int(input("Enter time: "))
si = (p * r * t) / 100
print("Simple Interest:", si)

#21. Check if a year is leap year.

year = int(input("Enter year: "))
if year % 4 == 0:
    print("Leap year")
else:
    print("Not a leap year")

#22. Remove spaces from a string.

text = input("Enter a string: ")
result = ""
i = 0
while i < len(text):
    if text[i] != " ":
        result = result + text[i]
    i = i + 1
print("Without spaces:", result)

#23. Print sum of numbers from 1 to n.

n = int(input("Enter a number: "))
total = 0
i = 1
while i <= n:
    total = total + i
    i = i + 1
print("Sum from 1 to", n, "is", total)

#24. Check if string is palindrome.

text = input("Enter a string: ")
reverse = ""
i = len(text) - 1
while i >= 0:
    reverse = reverse + text[i]
    i = i - 1
if text == reverse:
    print(text, "is a Palindrome")
else:
    print(text, "is not a Palindrome")

#25. Find factorial of a number.

num = int(input("Enter a number: "))
fact = 1
i = 1
while i <= num:
    fact = fact * i
    i = i + 1
print("Factorial of", num, "is", fact)

#26. Count digits in a number.

num = int(input("Enter a number: "))
temp = num
count = 0
while temp > 0:
    count = count + 1
    temp = temp // 10
print("Number of digits in", num, "is", count)

#27. Print all even numbers between 1 and 20.

i = 1
while i <= 20:
    if i % 2 == 0:
        print(i)
    i = i + 1

#28. Convert string to uppercase.

text = input("Enter a string: ")
result = ""
i = 0
while i < len(text):
    if text[i] >= "a" and text[i] <= "z":
        result = result + chr(ord(text[i]) - 32)
    else:
        result = result + text[i]
    i = i + 1
print("Uppercase:", result)

#29. Check if number is divisible by both 3 and 5.

num = int(input("Enter a number: "))
if num % 3 == 0 and num % 5 == 0:
    print(num, "is divisible by both 3 and 5")
else:
    print(num, "is not divisible by both 3 and 5")

#30. Find average of three numbers.

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
avg = (num1 + num2 + num3) / 3
print("Average:", avg)
