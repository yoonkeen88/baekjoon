import sys

class stack():
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
   


def main():
    n= int(sys.stdin.readline().strip())
    result = []
    st = stack()
    for _ in range(n):
        cmd = sys.stdin.readline().strip().split()

        if "push" in cmd:
            st.push(cmd[-1])
        elif "pop" in cmd:
            result.append(st.pop())

        elif "size" in cmd:
            result.append(st.size())

        elif "empty" in cmd:
            result.append(st.empty())

        elif "top" in cmd:
            result.append(st.top())
        

    sys.stdout.write("\n".join(map(str, result)) + "\n")

if __name__ == "__main__":
    main()
