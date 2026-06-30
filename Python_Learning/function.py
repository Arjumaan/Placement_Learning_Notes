''' 
A function is a block of code.
Performs a specific task.
can be used again and again
runs only when you call it

#Syntax

def function_name(parameters):
    """Docstring"""
    #code
    return value

EG:
'''
# def hello():
#     print("Hello World")

# hello()

# def greet(name):
#     print("Hello", name)

# greet("John")
# greet("Arjumaan")
# greet("Mr.Maan")

def add(a,b):
    return a+b

print(add(10,20))

def sub(a,b):
    return a-b

print(sub(20,10))

def mul(a,b):
    return a*b

print(mul(10,20))

def div(a,b):
    return a/b

print(div(20,10))
#----------------------------------------------------------------#

# 1️⃣ Write a function that returns the square of a number.

def square(n):
    return n ** 2

# 2️⃣ Write a function that returns the bigger number among two inputs.

def get_bigger(a, b):
    return a if a > b else b

# 3️⃣ Write a function that returns the total and average of three marks.

def total_and_average(m1, m2, m3):
    total = m1 + m2 + m3
    return total, total / 3

# 4️⃣ Create a function that checks whether a number is even or odd and returns the result.

def check_even_odd(n):
    return "Even" if n % 2 == 0 else "Odd"

# 5️⃣ Write a function that uses a local variable to store a message and return it.

def get_message():
    message = "Hello, this is a local variable message!"
    return message

# 6️⃣ Write a program with a global variable and a function that returns the value of that global variable.

global_message = "Hello, this is a global variable message!"

def get_global_message():
    return global_message

# 7️⃣ Write a function add(a, b) and another function square(n).
# Call them like: square(add(2,3)).

# def add(a, b): (Already defined above)
def add_nums(a, b):
    return a + b

# def square(n): (Already defined in question 1)
def square_num(n):
    return n ** 2

# Call them like:
print(square_num(add_nums(2, 3)))

# 8️⃣ Write a recursive function to return the factorial of a number.

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# 9️⃣ Write a recursive function to print numbers from 1 to n.

def print_1_to_n(n, current=1):
    if current > n:
        return
    print(current)
    print_1_to_n(n, current + 1)

# 🔟 Write a function that returns True if a string contains the letter 'a', otherwise False.

def contains_a(s):
    return 'a' in s
