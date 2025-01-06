import sys

def main():
    n = int(sys.stdin.readline().strip())
    li = list(map(int, sys.stdin.readline().split()))
    li.sort()
    time = 0
    for i in range(n):
        for j in range(i+1):
            time += li[j]
    print(time)
if __name__ == "__main__":
    main()
