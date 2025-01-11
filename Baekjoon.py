import sys

def main():
    dat = list(map(int, sys.stdin.read().strip().split("\n")))
    t = dat[0]  
    k = dat[1::2]  
    n = dat[2::2]  
    result = []

    max_k = max(k)
    max_n = max(n)
    dp = [[0] * (max_n + 1) for _ in range(max_k + 1)]

    for i in range(1, max_n + 1):
        dp[0][i] = i

    for i in range(1, max_k + 1):  
        for j in range(1, max_n + 1):  
            dp[i][j] = dp[i][j - 1] + dp[i - 1][j]

    for i in range(t):
        result.append(dp[k[i]][n[i]])

    sys.stdout.write("\n".join(map(str, result)) + "\n")

if __name__ == "__main__":
    main()
