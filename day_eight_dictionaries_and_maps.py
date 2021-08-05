# Task
# Given n names and phone numbers, assemble a phone book that maps friends' names to their respective phone numbers.
# You will then be given an unknown number of names to query your phone book for. For each name queried, print the
# associated entry from your phone book on a new line in the form name=phoneNumber;
# if an entry for name is not found, print Not found instead.

n = int(input())

phone_book = {}

for i in range(0, n):
    name, phone = input().split(' ')
    phone_book[name] = phone

for i in range(0, n):
    try:
        find_name = input()

        if find_name in phone_book:
            print(f"{find_name}={phone_book[find_name]}")
        else:
            print('Not found')

    except EOFError:
        break
        