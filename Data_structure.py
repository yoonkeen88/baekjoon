class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return -1

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            return -1

    def is_empty(self):
        return 1 if len(self.stack) == 0 else 0

    def size(self):
        return len(self.stack)
class Stack_2():
    def __init__(self):
        self.stack = []
    
    def push(self, value):
        self.stack.append(value)
        
    def pop(self):
        if self.stack:
            return self.stack.pop()
        else:
            return -1
    def size(self):
        return len(self.stack)
    def empty(self):
        return 0 if self.stack else 1
    
    def top(self):
        return self.stack[-1] if self.stack else -1
   

def vps(brackets):
    """
    괄호 문자열이 올바른지 판단하는 함수
    :param brackets: 괄호 문자열
    :return: 올바르면 "YES", 아니면 "NO"
    """
    st = []
    for char in brackets:
        if char == "(":
            st.append("(")
        elif char == ")":
            if st:
                st.pop()
            else:
                return "NO"
    return "YES" if not st else "NO"

def que_stack(n, line):
    """
    주어진 순서대로 뽑을 수 있는지 판단하는 함수
    :param n: n까지의 수
    :param line: 주어진 수열
    """
    other = []
    
    for current in range(1, n + 1):
        if line and line[0] == current:
            line.pop(0)
        elif other and other[-1] == current:
            other.pop()
        else:
            while line and line[0] != current:
                other.append(line.pop(0))
            if not line or line[0] != current:
                return "Sad"
            line.pop(0)
    return "Nice" if not other and not line else "Sad"

# 시간 복잡도 상 collections 에 deque 를 사용하도록.
from collections import deque
import sys

class Ma_queue:
    """
    큐를 구현한 클래스
    """
    def __init__(self):
        self.ma_queue = deque()

    def enqueue(self, n):
        self.ma_queue.append(n)

    def dequeue(self):
        if self.ma_queue:
            return self.ma_queue.popleft()
        else:
            return -1

    def is_empty(self):
        return 1 if not self.ma_queue else 0

    def size(self):
        return len(self.ma_queue)
    
    def back(self):
        if self.ma_queue:
            return self.ma_queue[-1]
        else:
            return -1

    def front(self):
        if self.ma_queue:
            return self.ma_queue[0]
        else:
            return -1
        
# 밑에는 내가 짠 것.
class Maqueue:
    """
    큐를 구현한 클래스
    """
    def __init__(self):
        # 큐를 빈 리스트로 초기화
        self.maqueue = []

    def enqueue(self, n):
        # 큐의 끝에 요소를 추가
        self.maqueue.append(n)

    def front(self):
        # 큐의 앞에 있는 요소를 반환
        if self.maqueue:
            return self.maqueue[0]
        else:
            return -1

    def dequeue(self):
        # 큐의 앞에서 요소를 제거하고 반환
        if self.maqueue:
            return self.maqueue.pop(0)
        else:
            return -1

    def is_empty(self):
        # 큐가 비어있는지 확인
        return 1 if len(self.maqueue) == 0 else 0

    def size(self):
        # 큐의 크기 반환
        return len(self.maqueue)
    
    def back(self):
        # 큐의 뒤에 있는 요소를 반환
        if self.maqueue:
            return self.maqueue[-1]
        else:
            return -1
### 하나 더 짠 Queue
class Queue_ma():
    def __init__(self):
        self.queue = []
    
    def push(self, value):
        self.queue.append(value)
        
    def pop(self):
        if self.queue:
            return self.queue.pop(0)
        else:
            return -1
    def size(self):
        return len(self.queue)
    def empty(self):
        return 0 if self.queue else 1
    def front(self):
        return self.queue[0] if self.queue else -1
    def back(self):
        return self.queue[-1] if self.queue else -1
    

### Deck Class 구현현
from collections import deque
class Deck:
    """
    Deck을 구현한 클래스
    속도 향상을 위해 deque를 사용
    """
    def __init__(self):
        self.deck = deque()

    def f_enqueue(self, n):     
        self.deck.appendleft(n)

    def l_enqueue(self, n):
        
        self.deck.append(n)

    def f_dequeue(self):
        if self.deck:
            return self.deck.popleft()
        else:
            return -1

    def l_dequeue(self):
        if self.deck:
            return self.deck.pop()
        else:
            return -1

    def front(self):
        if self.deck:
            return self.deck[0]
        else:
            return -1

    def back(self):
        if self.deck:
            return self.deck[-1]
        else:
            return -1

    def is_empty(self):
        
        return 1 if not self.deck else 0

    def size(self):
        return len(self.deck)
    

def least_bfs(graph, start, target, n):
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
