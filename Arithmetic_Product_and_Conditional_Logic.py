"""
Practice Problem: Write a Python function that accepts two integer numbers. 
If the product of the two numbers is less than or equal to 1000, return their product; 
otherwise, return their sum.

Exercise Purpose: Learn basic control flow and the use of if-else statements. 
Understand how code decisions change output based on a mathematical threshold.

Given Input:

    Case 1: number1 = 20, number2 = 30
    Case 2: number1 = 40, number2 = 30

Expected Output:

    The result is 600
    The result is 70
"""
def add_or_multiply(number1, number2):
    number_sum = number1 + number2
    number_multiply = number1 * number2
    if number1 * number2 <= 1000:
        return number_multiply
    else:
        return number_sum

def main():
    question1 = int(input("number1 = "))
    question2 = int(input("number2 = "))
    result = add_or_multiply(question1, question2)
    print(f"The result is {result}")

if __name__ == "__main__":
    main()
    

