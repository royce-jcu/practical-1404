import random

print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3
"""
What did you see on line 1?
What was the smallest number you could have seen, what was the largest?

Line 1 shows that it returned a random number between 5 and 20 inclusive.
The smallest number is 5 and the largest number is 20.
"""

"""
What did you see on line 2?
What was the smallest number you could have seen, what was the largest?
Could line 2 have produced a 4?

Line 2 shows that it returned a random odd number between 3 and 10 inclusive.
The smallest number is 3 and the largest number is 9.
Line 2 could not have produced a 4 because it must be odd number and it only produces 5 after 3. 
"""

"""
What did you see on line 3?
What was the smallest number you could have seen, what was the largest?

line 3 shows that it returned a random floating point number between 2.5 and 5.5.
The smallest number is 2.5 and the largest number is 5.5.
"""

"""
Write code, not a comment, to produce a random number between 1 and 100 inclusive.
"""
print(random.randint(1, 100))
