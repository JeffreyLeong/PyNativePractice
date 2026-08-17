"""
Practice Problem: Write a program that prints a number pattern using a while loop.

The pattern should start with 1 and increase by 2 for each new row. Each row should print 
the current number the same number of times as the row number.

Expected Pattern:

1
3 3
5 5 5
7 7 7 7
9 9 9 9 9

Exercise Purpose: Practice using a while loop, updating variables between iterations, and 
using a nested loop to control how many times each number is printed.
"""
rows = int(input("Enter the number of rows: "))

while rows:
    for i in range(rows):
        print(i)