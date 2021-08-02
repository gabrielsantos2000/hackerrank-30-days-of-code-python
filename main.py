from challenges import Challenges
#from day_4_class_vs_instance import Person

# To view the challenge response, just call the function
# Ex: challenges.day_three_intro_to_condition_statements()

challenges = Challenges()

t = int(input().strip())

for i in range(0, t):

    s = list(input().strip())
    str_par = ''
    str_impar = ''

    for j in range(0, len(s)):
        if j % 2 == 0:
            str_par += s[j]
        else:
            str_impar += s[j]
    else:
        print(str_par, str_impar)