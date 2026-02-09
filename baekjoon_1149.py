import sys 

input = sys.stdin.readline


        

def main():
    n = int(input().strip())
    arr = []
    for i in range(n):
        r,g,b = map(int, input().split())
        arr.append([r,g,b])
    for i in range(1,n):
        arr[i][0] += min(arr[i-1][1], arr[i-1][2])
        arr[i][1] += min(arr[i-1][0], arr[i-1][2])
        arr[i][2] += min(arr[i-1][0], arr[i-1][1])

    print(min(arr[n-1]))

main()