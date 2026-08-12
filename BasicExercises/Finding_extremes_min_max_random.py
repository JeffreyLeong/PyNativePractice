"""
Practice Problem: Given a list of random integers, find and print both the largest and the smallest numbers.

Exercise Purpose: This exercise explores “Aggregate Functions.” While Python has built-in tools for this, 
understanding how to identify extremes is critical for data normalization, where you often need to find the 
range of a dataset before processing it.

Given Input: nums = [45, 2, 89, 12, 7]

Expected Output: Largest: 89 Smallest: 2
"""
import random

unique_numbers = random.sample(range(1, 167), 8)

max_number = max(unique_numbers)
min_number = min(unique_numbers)

print(f"nums = {unique_numbers}")

print(f"\nLargest: {max_number} Smallest: {min_number}")
