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

# �ð� ���⵵ �� collections �� deque �� ����ϵ���.
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
        
# �ؿ��� ���� § ��.
class Maqueue:
    def __init__(self):
        # ť�� �� ����Ʈ�� �ʱ�ȭ
        self.maqueue = []

    def enqueue(self, n):
        # ť�� ���� ��Ҹ� �߰�
        self.maqueue.append(n)

    def front(self):
        # ť�� �տ� �ִ� ��Ҹ� ��ȯ
        if self.maqueue:
            return self.maqueue[0]
        else:
            return -1

    def dequeue(self):
        # ť�� �տ��� ��Ҹ� �����ϰ� ��ȯ
        if self.maqueue:
            return self.maqueue.pop(0)
        else:
            return -1

    def is_empty(self):
        # ť�� ����ִ��� Ȯ��
        return 1 if len(self.maqueue) == 0 else 0

    def size(self):
        # ť�� ũ�� ��ȯ
        return len(self.maqueue)
    
    def back(self):
        # ť�� �ڿ� �ִ� ��Ҹ� ��ȯ
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
        """?�� ?��료구�? �? 처음?�� ?��?���? ?��?��?��?�� ?��?��"""
        self.deck.appendleft(n)

    def l_enqueue(self, n):
        """?�� ?��료구�? �? 마�??막에 ?��?���? ?��?��?��?�� ?��?��"""
        self.deck.append(n)

    def f_dequeue(self):
        """?�� ?��료구�? �? 처음?�� ?��?���? ?��?���? 반환?���? ?��?��?��?�� ?��?��"""
        if self.deck:
            return self.deck.popleft()
        else:
            return -1

    def l_dequeue(self):
        """?�� ?��료구�? �? 마�??막에 ?��?���? ?��?���? 반환?���? ?��?��?��?�� ?��?��"""
        if self.deck:
            return self.deck.pop()
        else:
            return -1

    def front(self):
        """?�� ?��료구�? ?��?���? ?��?���? �? 처음 ?��?���? 반환?��?�� ?��?��"""
        if self.deck:
            return self.deck[0]
        else:
            return -1

    def back(self):
        """?�� ?��료구�? ?��?���? ?��?���? �? 마�??�? ?��?���? 반환?��?�� ?��?��"""
        if self.deck:
            return self.deck[-1]
        else:
            return -1

    def is_empty(self):
        """?�� ?��료구�? ?��?���? ?��?���? ?��?���? ?��?��.
        ?��?���? 1?�� ?��?���? 0?�� 반환"""
        return 1 if not self.deck else 0

    def size(self):
        """?�� ?��료구�? ?��?��즈�?? ?��?���? 반환"""
        return len(self.deck)