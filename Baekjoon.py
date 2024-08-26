import sys
# 시간 복잡도 상 collections 에 deque 를 사용하도록.
from collections import deque


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
        
def main():
    N = int(sys.stdin.read)
    
    my_que = list(range(1,N+1)) 
    for i in my_que:      
        if i % 2 ==0:
            my_que.append(my_que.popleft())
        else:
            my_que.popleft()
        
        if len(my_que)==1:
            break

    print(my_que[0])
        

if __name__ == "__main__":
    main()
