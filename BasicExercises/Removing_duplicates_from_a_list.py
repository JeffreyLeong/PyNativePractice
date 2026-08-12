"""
Practice Problem: Write a script that takes a list containing duplicate items and 
returns a new list with only unique elements.

Exercise Purpose: This exercise teaches “Data De-duplication.” In real-world data science, datasets are often 
“messy” with repeating entries. Mastering the conversion between Lists (which allow duplicates) and Sets (which do not) 
is the fastest way to clean data.

Given Input: data = [1, 2, 2, 3, 4, 4, 4, 5]

Expected Output: Unique List: [1, 2, 3, 4, 5]
"""
nums = []
while True:
    data = input("Enter a number (or type 'stop' to finish): ")
    try:
        if data == "stop":
            break
        nums.append(int(data))
    except ValueError:
        print("please try again")

unique_nums = list(set(nums))

print(f"\ndata = {nums}")
print(f"unique = {unique_nums}")
