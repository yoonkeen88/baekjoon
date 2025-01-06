import sys
from collections import Counter

def main():
    # 첫 번째 줄: 숫자의 개수
    n = int(sys.stdin.readline().strip())
    
    # 두 번째 줄부터: 숫자 하나씩 입력
    num = [int(sys.stdin.readline().strip()) for _ in range(n)]

    # 계산
    ran = max(num) - min(num)  # 범위
    me = round(sum(num) / n)  # 평균값
    counts = Counter(num)
    most_common = sorted(counts.items(), key=lambda x: (-x[1], x[0]))  # 빈도수 내림차순, 값 오름차순

    # 최빈값 구하기
    mo = most_common[0][0]
    
    # 최빈값이 2개 이상일 경우 두 번째로 작은 최빈값 찾기
    most_frequent = [value for value, count in most_common if count == most_common[0][1]]
    
    if len(most_frequent) > 1:  # 최빈값이 2개 이상일 경우
        second_mo = sorted(most_frequent)[1]  # 두 번째로 작은 값을 선택
    else:
        second_mo = mo  # 최빈값이 하나뿐이라면 기존 최빈값 사용

    # 중앙값 계산
    med = sorted(num)[n // 2]  # 중앙값

    # 결과 출력
    print(f"{me}\n{med}\n{second_mo}\n{ran}")

if __name__ == "__main__":
    main()
