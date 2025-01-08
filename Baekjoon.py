import sys


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
    


def main():
    n= int(sys.stdin.readline().strip())
    result = []
    st = Queue_ma()
    for _ in range(n):
        cmd = sys.stdin.readline().strip().split()

        if cmd[0] == "push":
            st.push(cmd[1])  # cmd[1]은 항상 존재
        elif cmd[0] == "pop":
            result.append(st.pop())
        elif cmd[0] == "size":
            result.append(st.size())
        elif cmd[0] == "empty":
            result.append(st.empty())
        elif cmd[0] == "front":
            result.append(st.front())
        elif cmd[0] == "back":
            result.append(st.back())
        

    sys.stdout.write("\n".join(map(str, result)) + "\n")

if __name__ == "__main__":
    main()
