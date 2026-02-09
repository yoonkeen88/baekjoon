import sys
from collections import deque
# please don't give me the answer directly
# I want to solve it by myself with little hints
# this is a dfs problem.

def dfs(start):
    visited[start] = True
    print(start, end=" ")
    for i in gr[start]:
        if not visited[i]:
            dfs(i)


def bfs(start):


    pass


input = sys.stdin.readline
n, m, start_point = map(int, input().split())
gr = [[] for _ in range(n+1)]
visited = [False] * (n+1)
queue = deque()
queue.append(start_point)

for i in range(m):
    a, b = map(int, input().split())
    if not a in gr[b] and not b in gr[a]:
        gr[a].append(b)
    
        gr[b].append(a)
    gr[a].sort()
    gr[b].sort()
    

dfs(start_point)
print()
visited = [False] * (n+1)
visited[start_point] = True
while queue:
    point = queue.popleft() 
    
    print(point, end = " ")
    for i in gr[point]:
        if not visited[i]:
            visited[i] = True

            queue.append(i)



# graph = []
# queue = deque()
# visited = [[-1] * m for _ in range(n)]

# for i in range(n):
#     graph.append(list(map(int, input().split())))
#     if 2 in graph[-1]:
#         queue.append((i,graph[-1].index(2)))
#         visited[i][graph[-1].index(2)] = 0  # 시작 지점은 거리 0

# for i in range(n):
#     for j in range(m):
#         if graph[i][j] == 0:
#             visited[i][j] = 0    # (중요!) 원래 갈 수 없는 땅(0)은 결과도 0이어야 함

# # 4. 방향 벡터 (상, 하, 좌, 우)
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]

# # 5. BFS 시작 (큐가 빌 때까지 반복)
# while queue:
#     x, y = queue.popleft() # 줄 맨 앞의 좌표 꺼내기 (현재 위치)
#     #  현 위치에서 4방향을 모두 탐색
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]

#         # 6. 유효성 검사 (여기가 핵심!)
#         # - 지도 범위를 벗어나지 않았는지?
#         # - 아직 방문하지 않은 곳인지? (visited[nx][ny] == -1 인지?)
#         # - 갈 수 있는 땅(1)인지? (사실 방문 안 한 곳 체크하면 이건 자동 해결될 수도?)
#         if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == -1:
#             if graph[nx][ny] == 1:
#                 visited[nx][ny] = visited[x][y] + 1 # 현재 거리 + 1칸
#                 queue.append((nx, ny)) # 다음에 여기서 또 출발해야 하니 큐에 등록

# # 출력 코드
# for row in visited:
#     print(*row)



