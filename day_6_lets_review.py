# Task
# Given a string, S, of length N that is indexed from 0 to N - 1, print its even-indexed and odd-indexed characters as
# space-separated strings on a single line (see the Sample below for more detail).

# Note: 0 is considered to be an even index.

t = int(input().strip())

for i in range(0, t):

    s = list(input().strip())
    str_pair = ''
    str_odd = ''

    for j in range(0, len(s)):
        if j % 2 == 0:
            str_pair += s[j]
        else:
            str_odd += s[j]
    else:
        print(str_pair, str_odd)
