# Task
# Given an integer, , perform the following conditional actions:

# If n is odd, print Weird
# If n is even and in the inclusive range of 2 to 5, print Not Weird
# If n is even and in the inclusive range of 6 to 20, print Weird
# If n is even and greater than 20, print Not Weird
# Complete the stub code provided in your editor to print whether or not  is weird.

# Explanation

# Sample Case 0: n = 3
# n is odd and odd numbers are weird, so we print Weird.

# Sample Case 1:
# n > 20 and n is even, so it is not weird. Thus, we print Not Weird.

# Difficulty: Easy
# Score: 30
# challenge link: https://www.hackerrank.com/challenges/30-conditional-statements/problem

N = int(input().strip())

if ((N < 1) or N % 2 != 0) or ((6 <= N <= 20) and N % 2 == 0):
    print('Weird')
else:
    print('Not Weird')
