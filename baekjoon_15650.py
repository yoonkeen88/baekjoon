import sys
# please don't give me the answer directly
# I want to solve it by myself with little hints
# this is a backtracking problem

input = sys.stdin.readline
n, m = map(int, input().split())



def back_tracking_not_squential(path):
    global visit
    if len(path) == m:
        print(' '.join(map(str, path)))
        return

    for i in range(1, n + 1):
        if visit[i]:
            continue

        visit[i] = True  
        path.append(i)
        back_tracking_not_squential(path)
        path.pop()
        visit[i] = False

visit = [False] * (n + 1)

def back_tracking(start, path):
    if len(path) == m:
        print(' '.join(map(str, path)))
        return

    for i in range(start, n + 1):
        path.append(i)
        back_tracking(i, path)
        path.pop()
back_tracking(1, [])



# back_tracking_not_squential([])
# back_tracking_not_squential([])