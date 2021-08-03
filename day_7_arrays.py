# Task
# Given an array, A, of N integers, print A's elements in reverse order 
# as a single line of space-separated numbers.

# Difficulty: Easy
# Score: 30
# Challenge link: https://www.hackerrank.com/challenges/30-arrays/problem

n = int(input().strip())

arr = list(map(int, input().rstrip().split()))

arr.reverse()

for i in range(0, n):
    print(arr[i], end=' ')
