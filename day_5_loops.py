# Task
# Given an integer, , print its first  multiples.
# Each multiple  (where ) should be printed on a new line in the form: n x i = result.

# Difficulty: Easy
# Score: 30
# Challenge link: https://www.hackerrank.com/challenges/30-loops/problem

n = int(input().strip())

if 2 <= n <= 20:
    for i in range(1, 11):
        result = n * i
        print(n, "x", i, "=", result)