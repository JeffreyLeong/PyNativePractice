"""
Practice Problem: Write a program to find how many times the substring “Emma” appears in a given string.

Exercise Purpose: Text analysis and pattern matching are core pillars of programming. 
This exercise introduces searching for a “needle in a haystack,” a fundamental concept for building search 
engines or data validation tools.

Given Input:

    str_x = "Emma is good developer. Emma is a writer"

Expected Output: Emma appeared 2 times
"""
str_x = "Emma is a good developer. Emma is a writer"
str_count = str_x.count("Emma")
print(f"Emma appeared {str_count} times")



# words = str_x.split()
# word_counts = {}
# for word in words:
#     if word in word_counts:
#         word_counts[word] += 1
# print(f"\n{word} appeared {word_counts} times")

