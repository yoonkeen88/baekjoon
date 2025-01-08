import sys

def main():
    # 입력 데이터 처리
    data = sys.stdin.read().splitlines()
    n = int(data[0])  # 첫 번째 줄은 개수
    points = [tuple(map(int, line.split())) for line in data[1:]]  # 이후 줄은 (weight, height)

    result = [1] * n  # 모든 사람의 초기 등수는 1 (등수는 낮을수록 높음)
    
    # 모든 쌍을 비교
    for i in range(n):
        for j in range(n):
            if i != j:  # 자기 자신과 비교 제외
                if points[i][0] < points[j][0] and points[i][1] < points[j][1]:
                    result[i] += 1  # i가 j보다 덩치가 작다면 등수 증가

    # 결과 출력
    sys.stdout.write(" ".join(map(str, result)) + "\n")

if __name__ == "__main__":
    main()
