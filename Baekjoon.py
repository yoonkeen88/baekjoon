import sys

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

t = int(sys.stdin.readline().strip())

output = []
for _ in range(t):
    line = sys.stdin.readline().strip()
    output.append(vps(line))

# 결과 출력
sys.stdout.write("\n".join(output) + "\n")
