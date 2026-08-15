"""
Practice Problem: Write a program that prints a pyramid pattern of numbers where each 
row starts at 1 and increases sequentially up to the row number.

Expected Pattern:

1
1 2
1 2 3
1 2 3 4
1 2 3 4 5

Exercise Purpose: This exercise builds on nested loops and introduces the concept of 
using the outer loop to control the number of elements in each row while the inner loop 
generates the sequential numbers within that row.

Given Input: Number of rows: 5

Expected Output: same as above
"""
rows = int(input("Enter a number of rows: "))

for i in range(1, rows + 1):
    for j in range(i):
        print(j+1,end=" ")
    print(" ")