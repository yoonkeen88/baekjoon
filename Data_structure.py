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
    

def vps(brackets):
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



import sys
from collections import deque

class Deck:
    def __init__(self):
        self.deck = deque()

    def f_enqueue(self, n):
        """?뜳 ?옄猷뚭뎄議? 留? 泥섏쓬?뿉 ?젙?닔瑜? ?엯?젰?븯?뒗 ?븿?닔"""
        self.deck.appendleft(n)

    def l_enqueue(self, n):
        """?뜳 ?옄猷뚭뎄議? 留? 留덉??留됱뿉 ?젙?닔瑜? ?엯?젰?븯?뒗 ?븿?닔"""
        self.deck.append(n)

    def f_dequeue(self):
        """?뜳 ?옄猷뚭뎄議? 留? 泥섏쓬?뿉 ?젙?닔媛? ?엳?떎硫? 諛섑솚?븯怨? ?궘?젣?븯?뒗 ?븿?닔"""
        if self.deck:
            return self.deck.popleft()
        else:
            return -1

    def l_dequeue(self):
        """?뜳 ?옄猷뚭뎄議? 留? 留덉??留됱뿉 ?젙?닔媛? ?엳?떎硫? 諛섑솚?븯怨? ?궘?젣?븯?뒗 ?븿?닔"""
        if self.deck:
            return self.deck.pop()
        else:
            return -1

    def front(self):
        """?뜳 ?옄猷뚭뎄議? ?젙?닔媛? ?엳?떎硫? 留? 泥섏쓬 ?젙?닔瑜? 諛섑솚?븯?뒗 ?븿?닔"""
        if self.deck:
            return self.deck[0]
        else:
            return -1

    def back(self):
        """?뜳 ?옄猷뚭뎄議? ?젙?닔媛? ?엳?떎硫? 留? 留덉??留? ?젙?닔瑜? 諛섑솚?븯?뒗 ?븿?닔"""
        if self.deck:
            return self.deck[-1]
        else:
            return -1

    def is_empty(self):
        """?뜳 ?옄猷뚭뎄議? ?젙?닔媛? ?엳?뒗吏? ?뾾?뒗吏? ?솗?씤.
        ?엳?떎硫? 1?쓣 ?뾾?떎硫? 0?쓣 諛섑솚"""
        return 1 if not self.deck else 0

    def size(self):
        """?뜳 ?옄猷뚭뎄議? ?궗?씠利덈?? ?젙?닔濡? 諛섑솚"""
        return len(self.deck)