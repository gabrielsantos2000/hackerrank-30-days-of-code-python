from challenges import Challenges
#from day_4_class_vs_instance import Person

# To view the challenge response, just call the function
# Ex: challenges.day_three_intro_to_condition_statements()

challenges = Challenges()

#challenges.day_four_class_vs_instance()

n = int(input().strip())

if 2 <= n <= 20:
    for i in range(1, 11):
        result = n * i
        print(n, "x", i, "=", result)
