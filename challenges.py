from personclass import Person


class Challenges:

    @staticmethod
    def day_zero_hello_world():
        phrase = input('Type a phrase: ')
        print('Hello, World.')
        print(phrase)

    @staticmethod
    def day_one_data_types():
        i = 4
        d = 4.0
        s = 'HackerRank'

        num1 = int(input('Enter a number: ').strip())
        num2 = int(input('Enter another number: ').strip())
        phrase = input('Type a phrase: ')

        print(i + num1)
        print(round(d + num2, 1))
        print(s, phrase)

    @staticmethod
    def day_two_operators():
        meal_cost = float(input('Enter the value of the meal: '))
        tip_percent = int(input('Enter the value of the tip percent: '))
        tax_percent = int(input('Enter the value of the tax percent: '))

        tip_percent = (tip_percent / 100) * meal_cost
        tax_percent = (tax_percent / 100) * meal_cost
        total_cost = meal_cost + tip_percent + tax_percent

        print(f'Total value of the meal: {round(total_cost)}')

    @staticmethod
    def day_three_intro_to_condition_statements():
        num = int(input('Enter a number: ').strip())

        if ((num < 1) or num % 2 != 0) or ((6 <= num <= 20) and num % 2 == 0):
            print('Weird')
        else:
            print('Not Weird')

    def day_four_class_vs_instance(self):
        t = int(input('Enter the amount of times to calculate the age: '))
        age = int(input())
        p = Person(age)
        p.amIOld()
        for j in range(0, 3):
            p.yearPasses()
        p.amIOld()
        print("")