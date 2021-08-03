n = int(input().strip())

arr = list(map(int, input().rstrip().split()))

arr.reverse()

for i in range(0, n):
    print(arr[i], end=' ')
