import sys
from collections import defaultdict, deque

def bfs(graph, start, target, n):
    """
    BFS로 시작 노드에서 목표 노드까지의 최단 거리를 계산
    """
    visited = [False] * (n + 1)
    distance = [-1] * (n + 1)
    queue = deque([start])

    visited[start] = True # 방문한 노드 표시 중복되는 노드 방문은 하지 않음
    distance[start] = 0 # 시작점 거리는 0

    while queue:
        node = queue.popleft() # queue 자료 구조니까 제일 먼 있는걸 제외
        for neighbor in graph[node]:
            if not visited[neighbor]:
                queue.append(neighbor)
                visited[neighbor] = True
                distance[neighbor] = distance[node] + 1
                if neighbor == target:
                    return distance[target]

    return -1  # 목표 노드에 도달할 수 없는 경우


def main():
    import sys
    from collections import defaultdict, deque

    input = sys.stdin.read().strip().split("\n")
    n, m = map(int, input[0].split())

    # 그래프 초기화
    graph = defaultdict(list)
    for line in input[1:]:
        a, b = map(int, line.split())
        graph[a].append(b)
        graph[b].append(a)

    def least_bfs(start):
        """start에서 모든 노드까지 최단 거리의 합 계산"""
        visited = [False] * (n + 1)
        distance = [0] * (n + 1)
        queue = deque([start])
        visited[start] = True

        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    distance[neighbor] = distance[node] + 1
                    queue.append(neighbor)

        return sum(distance[1:])  # 1번 노드부터 시작

    # 각 노드의 케빈 베이컨 수 계산
    results = []
    for i in range(1, n + 1):
        results.append((least_bfs(i), i))  # (케빈 베이컨 수, 노드 번호)

    # 정렬: 케빈 베이컨 수 오름차순, 노드 번호 오름차순
    results.sort(key=lambda x: (x[0], x[1]))

    # 결과 출력
    print(results[0][1])


if __name__ == "__main__":
    main()
