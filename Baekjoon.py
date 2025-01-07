import sys

def main():
    input = sys.stdin.read
    data = input().split()

    n = int(data[0])  # 첫 번째 줄의 숫자 개수
    a_li = set(map(int, data[1:n+1]))  # 두 번째 줄의 숫자들 (집합으로 변환)
    m = int(data[n+1])  # 세 번째 줄의 숫자 개수
    b_li = map(int, data[n+2:])  # 네 번째 줄의 숫자들

    # 결과 리스트 생성
    result = [1 if i in a_li else 0 for i in b_li]

    # 결과 출력
    sys.stdout.write('\n'.join(map(str, result)) + '\n')


if __name__ == "__main__":
    main()
