import sys

def main():
    # 입력
    n, m = map(int, input().strip().split())
    arr = list(map(int, sys.stdin.readline().strip().split()))
  
    prefix_sum = [0] * (n+1)
    for i in range(1, n+1):
        prefix_sum[i] = prefix_sum[i - 1] + arr[i - 1]
    
    results = []
    for _ in range(m):
        i, j = map(int, input().strip().split())
        results.append(prefix_sum[j] - prefix_sum[i - 1])

    sys.stdout.write("\n".join(map(str, results)) + "\n")
if __name__ == "__main__":
    main()
