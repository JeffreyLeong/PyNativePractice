"""
Practice Problem: Iterate through a given list of numbers and print only those numbers which are divisible by 5.

Exercise Purpose: This exercise teaches the use of the modulo operator (%) and loop filtering. 
In data processing, you often need to sift through large datasets to extract subsets that meet mathematical criteria.

Given Input: num_list = [10, 20, 33, 46, 55]

Expected Output:

Divisible by 5:
10, 20, 55
"""
num_list = input("Enter numbers separated by a space: ")

print("Divisable by 5:")
for number in num_list.split():
    number = int(number)
    if number % 5 == 0:
        print(f"{number}", end=" ")


