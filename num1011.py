import math

test = int(input())
for _ in range(test):
    x, y = map(int, input().split())
    dis = y - x
    n = int(math.sqrt(dis))
    if dis == n * n:
        print(2 * n - 1)
    elif dis <= n * n + n:
        print(2 * n)
    else:
        print(2 * n + 1)