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
N = int(input())

# 스택 객체 생성
my_stack = Stack()

for _ in range(N):
    line = sys.stdin.readline.rstrip()
    command = int(line[0])
    
    if command == 1:
        my_stack.push(int(line[1]))
    elif command == 2:
        print(my_stack.pop())
    elif command == 3:
        print(my_stack.size())
    elif command == 4:
        print(my_stack.is_empty())
    elif command == 5:
        print(my_stack.peek())
