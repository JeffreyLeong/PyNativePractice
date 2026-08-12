"""
Practice Problem: Write a program that takes a string from the user, counts how many times each word appears, 
and identifies the most frequently occurring word(s) and their frequency.

Exercise Purpose: This exercise introduces word-frequency analysis using string manipulation, loops, 
dictionaries, and conditional logic. It demonstrates how to process unstructured text, count occurrences 
of individual words, and identify the highest frequency within a collection of data.

Given Input:

    str_x = "Emma is good developer. Emma is a writer"

Expected Output: 
Most Frequent word(s):
'Emma' appeared 2 times
'is' appeared 2 times
"""
str_x = input("Enter a string. I will count the duplicates: \n\t")

words = str_x.split()
word_counts = {}

for word in words:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

print("\nMost Frequent word(s):")

for word, count in word_counts.items():
    if count == max(word_counts.values()):
        print(f"'{word}' appeared {count} times")