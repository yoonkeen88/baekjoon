import sys

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

# 명령어의 수 입력
k = int(sys.stdin.readline())

# 스택 객체 생성
my_stack = Stack()

output = []

for _ in range(k):
    line = sys.stdin.readline().split()
    command = int(line[0])
    
    if command != 0:
        my_stack.push(int(command))
    else :
        my_stack.pop()

for i in range(k):
    sum += my_stack[i]

# 결과 출력
sys.stdout.write(sum)
