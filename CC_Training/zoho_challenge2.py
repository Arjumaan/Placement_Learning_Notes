'''
Question:

	Write a program to sort the elements in odd positions in descending order and elements in ascending order

Eg 1: Input: 13,2,4,15,12,10,5
Output: 13,2,12,10,5,15,4
Eg 2: Input: 1,2,3,4,5,6,7,8,9
Output: 9,2,7,4,5,6,3,8,1
'''

arr = list(map(int, input("Enter numbers separated by commas: ").split(',')))

odd = sorted(arr[::2], reverse=True)
even = sorted(arr[1::2])

result = []

for i in range(len(odd)):
    result.append(odd[i])
    if i < len(even):
        result.append(even[i])

print(result)