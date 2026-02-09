import sys
input = sys.stdin.readline
n, m = map(int, sys.stdin.readline().split())
li = list(map(int, input().split()))
li.sort()
def back_tracking_not_squential(path):
    global visit
    if len(path) == m:
        print(' '.join(map(str, path)))
        return

    for i in range(0, n):
        if visit[i]:
            continue

        visit[i] = True # 다음 재귀 내부에서 사용하지 못하게 처리
        path.append(li[i])
        back_tracking_not_squential(path)
        path.pop()
        visit[i] = False # 원상 복구를 위한 처리

visit = [False] * (n + 1)
back_tracking_not_squential([])