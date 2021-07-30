# Task
# Given the meal price (base cost of a meal), tip percent (the percentage of the meal price being added as tip),
# and tax percent (the percentage of the meal price being added as tax) for a meal, find and print the meal's total cost.
# Round the result to the nearest integer

# Difficulty: Easy
# Score: 30
# challenge link: https://www.hackerrank.com/challenges/30-operators/problem

meal_cost = float(input())
tip_percent = int(input())
tax_percent = int(input())

tip_percent = (tip_percent / 100) * meal_cost
tax_percent = (tax_percent / 100) * meal_cost
total_cost = meal_cost + tip_percent + tax_percent

print(round(total_cost))
