#List notes
#Q1 Create a list using user input and display it.
n = int(input("Enter the number of elements: "))
lst = []

for i in range(n):
    value = int(input("Enter elements: "))
    lst.append(value)

print("The list is: ", lst)

#Q2