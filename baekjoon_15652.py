import sys

n, m = map(int, sys.stdin.readline().split())
def back_tracking(start, path):
    if len(path) == m:
        print(' '.join(map(str, path)))
        return

    for i in range(start, n + 1):
        path.append(i)
        back_tracking(i, path)
        path.pop()
back_tracking(1, [])