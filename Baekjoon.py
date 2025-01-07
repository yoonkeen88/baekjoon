import sys
from bisect import bisect_left

def binary_search(array, target):
    index = bisect_left(array, target)  # target의 삽입 위치를 찾음
    if index < len(array) and array[index] == target:
        return True
    return False

def main1():
    n = int(sys.stdin.readline().strip())
    a_li = sorted(map(int, sys.stdin.readline().strip().split()))  # 정렬
    m = int(sys.stdin.readline().strip())
    b_li = list(map(int, sys.stdin.readline().strip().split()))
    
    result = ['1' if binary_search(a_li, x) else '0' for x in b_li]
    sys.stdout.write('\n'.join(result) + '\n')


def main():
    input = sys.stdin.read
    data = input().split()

    n = int(data[0])  # 첫 번째 줄의 숫자 개수
    a_li = set(map(int, data[1:n+1]))  # 두 번째 줄의 숫자들 (집합으로 변환)
    m = int(data[n+1])  # 세 번째 줄의 숫자 개수
    b_li = map(int, data[n+2:])  

    result = [1 if i in a_li else 0 for i in b_li]

    # 결과 출력
    sys.stdout.write('\n'.join(map(str, result)) + '\n')


if __name__ == "__main__":
    main()
    main1()






