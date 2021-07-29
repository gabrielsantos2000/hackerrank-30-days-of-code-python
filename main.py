from challenges import Challenges

challenges = Challenges()

# Day 2: Operators
def solve(meal_cost, tip_percent, tax_percent):
    print(challenges.dayTwoOperators(meal_cost, tip_percent, tax_percent))
solve('12.00', '20', '8')