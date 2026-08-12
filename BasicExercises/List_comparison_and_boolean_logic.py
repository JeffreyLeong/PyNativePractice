"""
Practice Problem: Write a function to return True if the first and last number of a given list 
is the same. If the numbers are different, return False.

Exercise Purpose: This exercise introduces “Collection Indexing” and “Boolean Flags.” 
Comparing data structure boundaries is common in pattern matching and data integrity checks.

Given Input:

    numbers_x = [10, 20, 30, 40, 10]
    numbers_y = [75, 65, 35, 75, 30]

Expected Output:

Given list: [75, 65, 35, 75, 30] | result is False
Given list: [10, 20, 30, 40, 10] | result is True
"""
def true_or_false(num_list):
    return num_list[0] == num_list[-1]

numbers = []
data = int(input("How many numbers do you want to list? "))
for i in range(data):
    num = int(input(f"Enter number {i + 1}: "))
    numbers.append(num)

print(true_or_false(numbers))