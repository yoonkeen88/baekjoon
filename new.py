import sys
def main():
    # 입력
    n, m = map(int, input().strip().split())
    arr = list(map(int, sys.stdin.readline().strip().split()))
    
    # 누적 합 배열 생성
    prefix_sum = [0] * (n+1)
    for i in range(1, n+1):
        prefix_sum[i] = prefix_sum[i - 1] + arr[i - 1]
    
    results = []
    for quiz in data[n + 1:]:
        if quiz.isdigit():
            results.append(reverse_poket[int(quiz)])
        else:
            results.append(poket[quiz])

    sys.stdout.write("\n".join(map(str, results))+"\n")

if __name__ == "__main__":
    main()
