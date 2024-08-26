import sys

def pop_origin(n, line):
    other = []
    
    for current in range(1, n + 1):
        # current에 해당하는 학생이 line의 맨 앞에 있는 경우
        if line and line[0] == current:
            line.pop(0)
        # current에 해당하는 학생이 other의 맨 위에 있는 경우
        elif other and other[-1] == current:
            other.pop()
        # line에서 current를 찾지 못한 경우
        else:
            # line에서 current를 찾을 때까지 other로 이동
            while line and line[0] != current:
                other.append(line.pop(0))
            # 만약 line이 비어있거나 current를 찾지 못한 경우 처리
            if not line or line[0] != current:
                return "Sad"
            # current를 찾은 경우 pop
            line.pop(0)
    
    # 남은 것이 없으면 Nice, 아니면 Sad
    return "Nice" if not other and not line else "Sad"

def main():
    N = int(input())
    line = list(map(int, sys.stdin.read().split()))  # 정수 리스트로 변환
    
    result = pop_origin(N, line)
    print(result)

if __name__ == "__main__":
    main()
