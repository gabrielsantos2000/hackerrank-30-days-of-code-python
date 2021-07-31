from personclass import Person

# Task
# Write a Person class with an instance variable, age, and a constructor that takes an integer, , as a parameter.
# The constructor must assign initialAge to age after confirming the argument passed as initialAge is not negative;
# if a negative argument is passed as initialAge,
# the constructor should set age to 0 and print Age is not valid, setting age to 0..
# In addition, you must write the following instance methods:
#
# yearPasses() should increase the age instance variable by 1.
# amIOld() should perform the following conditional actions:
#   If age < 13, print You are young..
#   If age >= 13 and age < 18, print You are a teenager..
# Otherwise, print You are old..

# Difficulty: Easy
# Score: 30
# Challenge link: https://www.hackerrank.com/challenges/30-class-vs-instance/problem

t = int(input())
for i in range(0, t):
    age = int(input())
    p = Person(age)
    p.amIOld()
    for j in range(0, 3):
        p.yearPasses()
    p.amIOld()
    print("")