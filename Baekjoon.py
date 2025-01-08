import sys

def main():
    # 입력 데이터 처리
    # n: 랜선의 갯수, k: 잘라야하는 횟수

    n,k = map(int, sys.stdin.readline().split())
    data = list(sys.stdin.read().splitlines())
    result =[]
    for i in data:
        for j in range(1,k-n+1):
            result.append([int(i)//j,j])

    
    sys.stdout.write(" ".join(map(str, result)) + "\n")

if __name__ == "__main__":
    main()
