import sys

def main():
    n, k = map(int, sys.stdin.readline().strip().split())
    se = set()
    full = set(map(str, range(1, 21)))  # 미리 전체 집합 생성
    result = []
    for _ in range(n):
        name = sys.stdin.readline().strip()
        se.add(name)

    for _ in range(k):
        name = sys.stdin.readline().strip()
        if name in se:
            result.append(name)
    result.sort()
    print(len(result))
    print("\n".join(result))



if __name__ == "__main__":
    main()
