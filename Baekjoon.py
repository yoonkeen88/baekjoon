def main():
    # 입력
    n = int(input().strip())
    
    if n == 0:  # n이 0일 경우 바로 출력
        print(0)
        return
    
    # dp 배열 초기화
    dp = [0] * (max(3, n + 1))  # n이 2보다 작아도 dp[2]를 초기화하기 위해 크기를 최소 3으로 설정
    dp[1] = 1
    dp[2] = 2

    division = 10007
    if n > 2:
        for i in range(3, n + 1):
            dp[i] = (dp[i - 1] + dp[i - 2]) % division
        print(dp[n])
    elif n == 1:
        print(dp[1])
    elif n == 2:
        print(dp[2])

if __name__ == "__main__":
    main()
