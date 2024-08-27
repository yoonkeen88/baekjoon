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

# ½Ã°£ º¹Àâµµ »ó collections ¿¡ deque ¸¦ »ç¿ëÇÏµµ·Ï.
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
        
# ¹Ø¿¡´Â ³»°¡ Â§ °Í.
class Maqueue:
    def __init__(self):
        # Å¥¸¦ ºó ¸®½ºÆ®·Î ÃÊ±âÈ­
        self.maqueue = []

    def enqueue(self, n):
        # Å¥ÀÇ ³¡¿¡ ¿ä¼Ò¸¦ Ãß°¡
        self.maqueue.append(n)

    def front(self):
        # Å¥ÀÇ ¾Õ¿¡ ÀÖ´Â ¿ä¼Ò¸¦ ¹İÈ¯
        if self.maqueue:
            return self.maqueue[0]
        else:
            return -1

    def dequeue(self):
        # Å¥ÀÇ ¾Õ¿¡¼­ ¿ä¼Ò¸¦ Á¦°ÅÇÏ°í ¹İÈ¯
        if self.maqueue:
            return self.maqueue.pop(0)
        else:
            return -1

    def is_empty(self):
        # Å¥°¡ ºñ¾îÀÖ´ÂÁö È®ÀÎ
        return 1 if len(self.maqueue) == 0 else 0

    def size(self):
        # Å¥ÀÇ Å©±â ¹İÈ¯
        return len(self.maqueue)
    
    def back(self):
        # Å¥ÀÇ µÚ¿¡ ÀÖ´Â ¿ä¼Ò¸¦ ¹İÈ¯
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
        """?± ?ë£Œêµ¬ì¡? ë§? ì²˜ìŒ?— ? •?ˆ˜ë¥? ?…? ¥?•˜?Š” ?•¨?ˆ˜"""
        self.deck.appendleft(n)

    def l_enqueue(self, n):
        """?± ?ë£Œêµ¬ì¡? ë§? ë§ˆì??ë§‰ì— ? •?ˆ˜ë¥? ?…? ¥?•˜?Š” ?•¨?ˆ˜"""
        self.deck.append(n)

    def f_dequeue(self):
        """?± ?ë£Œêµ¬ì¡? ë§? ì²˜ìŒ?— ? •?ˆ˜ê°? ?ˆ?‹¤ë©? ë°˜í™˜?•˜ê³? ?‚­? œ?•˜?Š” ?•¨?ˆ˜"""
        if self.deck:
            return self.deck.popleft()
        else:
            return -1

    def l_dequeue(self):
        """?± ?ë£Œêµ¬ì¡? ë§? ë§ˆì??ë§‰ì— ? •?ˆ˜ê°? ?ˆ?‹¤ë©? ë°˜í™˜?•˜ê³? ?‚­? œ?•˜?Š” ?•¨?ˆ˜"""
        if self.deck:
            return self.deck.pop()
        else:
            return -1

    def front(self):
        """?± ?ë£Œêµ¬ì¡? ? •?ˆ˜ê°? ?ˆ?‹¤ë©? ë§? ì²˜ìŒ ? •?ˆ˜ë¥? ë°˜í™˜?•˜?Š” ?•¨?ˆ˜"""
        if self.deck:
            return self.deck[0]
        else:
            return -1

    def back(self):
        """?± ?ë£Œêµ¬ì¡? ? •?ˆ˜ê°? ?ˆ?‹¤ë©? ë§? ë§ˆì??ë§? ? •?ˆ˜ë¥? ë°˜í™˜?•˜?Š” ?•¨?ˆ˜"""
        if self.deck:
            return self.deck[-1]
        else:
            return -1

    def is_empty(self):
        """?± ?ë£Œêµ¬ì¡? ? •?ˆ˜ê°? ?ˆ?Š”ì§? ?—†?Š”ì§? ?™•?¸.
        ?ˆ?‹¤ë©? 1?„ ?—†?‹¤ë©? 0?„ ë°˜í™˜"""
        return 1 if not self.deck else 0

    def size(self):
        """?± ?ë£Œêµ¬ì¡? ?‚¬?´ì¦ˆë?? ? •?ˆ˜ë¡? ë°˜í™˜"""
        return len(self.deck)