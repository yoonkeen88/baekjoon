import sys
from collections import defaultdict
from collections import deque

def shortest_path_bfs(graph, start, target):
    """
    BFS를 사용하여 시작 노드에서 목표 노드까지의 최단 경로를 찾음.
    :param graph: 인접 리스트로 표현된 그래프
    :param start: 시작 노드
    :param target: 목표 노드
    :return: 최단 경로 거리
    """
    visited = [False] * (len(graph) + 1)
    distance = [-1] * (len(graph) + 1)  # 거리를 기록 (-1은 방문하지 않았음을 의미)
    queue = deque([start])

    visited[start] = True
    distance[start] = 0  # 시작 노드의 거리는 0

    while queue:
        node = queue.popleft()

        for neighbor in graph[node]:
            if not visited[neighbor]:
                queue.append(neighbor)
                visited[neighbor] = True
                distance[neighbor] = distance[node] + 1  # 이전 노드 거리 + 1
                
                if neighbor == target:  # 목표 노드에 도달하면 종료
                    return distance[target]

    return -1  # 목표 노드에 도달할 수 없는 경우

# dfs 는 스택(재귀 형식)
def dfs(graph, start, visited):
    """
    그래프를 깊이 우선 탐색하는 함수.
    :param graph: 인접 리스트로 표현된 그래프
    :param start: 시작 노드
    :param visited: 방문 여부를 기록하는 리스트
    """
    visited[start] = True  # 현재 노드를 방문
    print(start, end=' ')  # 방문한 노드를 출력

    for neighbor in graph[start]:  # 현재 노드의 모든 인접 노드를 탐색
        if not visited[neighbor]:  # 아직 방문하지 않았다면
            dfs(graph, neighbor, visited)  # 재귀적으로 방문



def main():
    # 변수 입력
    n,m = map(int, sys.stdin.readline().strip().split())


    # r 이라는 변수에 [0]*n 을 할당하고 
    # gr = [r for _ in range(n)] 을 하더라도
    # 참조만 되어 참사가 일어날 수도.
    
    # gr = [[0]*n]*n # 앝은 복사 임으로 원하는데로 되지 않음

     # 그래프 초기화
    graph = defaultdict(list)
    for _ in range(m):
        i, j = map(int, sys.stdin.readline().strip().split())
        graph[i].append(j)

    # 각 노드에서 다른 모든 노드로의 최단 거리 합 계산
    result = [0] * n
    for i in range(1, n + 1):
        total_distance = 0
        for j in range(1, n + 1):
            if i != j:  # 자기 자신으로 가는 경로는 계산하지 않음
                distance = shortest_path_bfs(graph, i, j)
                if distance != -1:  # 도달 가능한 경우에만 거리 합산
                    total_distance += distance
        result[i - 1] = total_distance

    # 최단 경로 합이 가장 작은 노드 출력
    print(min(result))

if __name__ == "__main__":
    main()
