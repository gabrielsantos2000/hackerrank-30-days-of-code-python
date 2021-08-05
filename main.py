from challenges import Challenges

# from day_4_class_vs_instance import Person

# To view the challenge response, just call the function
# Ex: challenges.day_three_intro_to_condition_statements()

challenges = Challenges()

n = int(input())

phoneBook = {}

for i in range(0, n):
    name, phone = input().split(' ')
    phoneBook[name] = phone

for i in range(0, n):
    try:
        findName = input()

        if findName in phoneBook:
            print(f"{findName}={phoneBook[findName]}")
        else:
            print('Not found')

    except EOFError:
        break
