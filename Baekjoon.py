import sys
from collections import Counter

def main():
    data = sys.stdin.read().splitlines()
    n = int(data[0])
    card = list(map(int, data[1:n+2]))
    m = int(data[n+2])
    target = list(map(int, data[n+3].split()))
    
    # `card`의 각 숫자 빈도 계산
    card_count = Counter(card)
    
    # 결과 계산
    result = [card_count[i] for i in target]

    # 결과 출력
    sys.stdout.write("\n".join(map(str, result)) + "\n")

if __name__ == "__main__":
    main()
