"""
Inverted pyramid pattern of numbers

An inverted pyramid is a downward pattern where numbers get reduced in each iteration, 
and on the last row, it shows only one number. Use reverse for loop to print this pattern.

Pattern

1 1 1 1 1 
2 2 2 2 
3 3 3 
4 4 
5
# """
rows = int(input("Enter the number of rows: "))
b = 0

for i in range(rows, 0, -1):
    b += 1
    for j in range(1, i+1):
        print(b, end=" ")
    print("")
