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

    def is_empty(self):
        return len(self.stack) == 0

while True:
    line = sys.stdin.readline().strip()
    if line[0] == ".":
        break
    
    big = Stack()
    small = Stack()

    balanced = True  # 균형 상태를 추적하기 위한 변수

    for i in line:
        if i == "(":
            small.push("(")
        elif i == "[":
            big.push("[")
        elif i == ")":
            if small.pop() == -1:
                balanced = False
                break
        elif i == "]":
            if big.pop() == -1:
                balanced = False
                break
    
    # 모든 괄호가 짝을 이루고 있는지 확인
    if balanced and small.is_empty() and big.is_empty():
        print("yes")
    else:
        print("no")
