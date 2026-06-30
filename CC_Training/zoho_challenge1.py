''' 
Question:

Write a program to give the following output for the given input.

Eg 1: Input: a1b10
Output: abbbbbbbbbb
Eg: 2: Input: b3c6d15
Output: bbbccccccddddddddddddddd
The number varies from 1 to 99.
'''

def expand_string(s):
    result = ""
    i = 0

    while i < len(s):
        ch = s[i]
        i += 1

        num = ""
        while i < len(s) and s[i].isdigit() and int(s[i]) < 99:
            num += s[i]
            i += 1

        result += ch * int(num)

    return result

s = input("Enter a string: ")
print(f"Given String : {s}")
print(f"Expanded String : {expand_string(s)}")