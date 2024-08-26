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
