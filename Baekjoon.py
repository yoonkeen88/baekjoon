import sys

def main():
    # 테스트 케이스 개수 입력
    t = int(sys.stdin.readline().strip())
    
    for _ in range(t):
        # 숫자 n 입력
        n = int(sys.stdin.readline().strip())
        
        # DP 배열 초기화
        dp = [0] * (n + 1)
        dp[0] = 1  # 0을 만드는 경우는 1가지 (아무것도 더하지 않는 경우)
        
        if n >= 1:
            dp[1] = 1  # 1을 만드는 경우는 1가지 (1)
        if n >= 2:
            dp[2] = 2  # 2를 만드는 경우는 2가지 (1+1, 2)
        
        # 점화식을 이용하여 DP 계산
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
        
        # 결과 출력
        print(dp[n])

if __name__ == "__main__":
    main()
