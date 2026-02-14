#-----------------------------
#Level 1 Practice Questions!
#-----------------------------

#1. Write a program to convert user input to integer and add 10.
num1 = int(input("Enter a number: "))
print(num1 + 10)

#2. Write a program to get a number as input, convert it into a float, and print it.
num2 = float(input("Enter a number: "))
print(num2)

#3. Write a program to create a variable x and assign it the value 10 and print the type of x.
x = 10
print(type(x))

#4. A mobile phone costs 15999.50. Add GST of 500 and display the total price along with its datatype.
mobile_price = 15999.50
gst = 500
total_price = mobile_price + gst
print(total_price)
print(type(total_price))

#5. Write a program to convert number to string.
num = 10
str_num = str(num)
print(str_num)
print(type(str_num))

#6. Write a example for implicit conversion.
num1 = 10
num2 = 20.5
print(num1 + num2)
print(type(num1 + num2))

#7. Write a example for explicit conversion.
num1 = "10"
num2 = "20.5"
print(int(num1) + float(num2))
print(type(int(num1) + float(num2)))

#8. Identify the datatype: 
a = True
print(type(a))

#9. Create a dictionary to store student details (name, age, marks) and print it.
student = {
    "name": "Arjumaan",
    "age": 21,
    "marks": 90
}
print(student)

#10. Create a set with duplicate values and print it.
my_set = {1, 2, 3, 4, 4, 4, 4, 5}
print(my_set)