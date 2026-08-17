"""
Practice Problem: Write a program that prints an inverted pyramid pattern of sequential numbers.

The pattern should start with the numbers 0 through 5 on the first row. Each subsequent row should 
contain one fewer number, while always starting from 0.

Expected Pattern:

0 1 2 3 4 5
0 1 2 3 4
0 1 2 3
0 1 2
0 1

Exercise Purpose: Practice nested loops and reverse iteration. Use the outer loop to control 
the decreasing number of elements in each row, and use the inner loop to generate the sequential 
numbers starting from 0.
"""
rows = int(input("Enter the number of rows: "))

for i in range(rows, 0, -1):
    for j in range(i+1):
        print(j, end=" ")
    print(" ")