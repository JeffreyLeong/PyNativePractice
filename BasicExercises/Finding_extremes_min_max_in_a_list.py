"""
Practice Problem: Given a list of integers, find and print both the largest and the smallest numbers.

Exercise Purpose: This exercise explores “Aggregate Functions.” While Python has built-in tools for this, 
understanding how to identify extremes is critical for data normalization, where you often need to find the 
range of a dataset before processing it.

Given Input: nums = [45, 2, 89, 12, 7]

Expected Output: Largest: 89 Smallest: 2
"""
number_input = input("Enter numbers seperated by a space: ")
nums = []

for number in number_input.split():
    nums.append(int(number))

max_num = max(nums)
min_num = min(nums)

print(f"nums = {nums}")
print(f"\nLargest: {max_num} Smallest: {min_num}")
