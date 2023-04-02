"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""
"""
1. A ValueError will occur when the user's input is string or a float number. 

2. A ZeroDivisionError will occur when the user's input for the denominator is zero.

3. To avoid the possibility of a ZeroDivisionError, we can use if/else statement to print an error message if 
the denominator is zero.
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    if denominator == 0:
        print("Cannot divide by zero!")
    else:
        fraction = numerator / denominator
        print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")

print("Finished.")
