"""
Inverted Pyramid pattern with the same digit, reverse loop

Pattern: –

5 5 5 5 5 
5 5 5 5 
5 5 5 
5 5 
5
"""
rows = int(input("Enter the number of rows: "))

for i in range(rows, 0, -1):
    for j in range(i):
        print(rows, end=" ")
    print(" ")