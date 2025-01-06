import sys

def main():
    n = int(sys.stdin.readline().strip())
    se = set()
    full = set(map(str, range(1, 21)))  # 미리 전체 집합 생성

    for _ in range(n):
        command = sys.stdin.readline().strip().split()
        if command[0] == "all":
            se = full.copy()
        elif command[0] == "empty":
            se = set()
        else:
            cmd, num = command[0], command[1]
            if cmd == "add":
                se.add(num)
            elif cmd == "remove":
                se.discard(num)
            elif cmd == "check":
                print(1 if num in se else 0)
            elif cmd == "toggle":
                if num in se:
                    se.remove(num)
                else:
                    se.add(num)

if __name__ == "__main__":
    main()
