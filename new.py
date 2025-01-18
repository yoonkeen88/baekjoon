import sys

def main():
    # 입력 처리
    input_data = sys.stdin.read().strip().split("\n")
    n = int(input_data[0])  # 첫 번째 줄: 단어 개수
    dat = input_data[1:]    # 이후 줄: 단어 리스트
    
    cnt = 0  # 그룹 단어가 아닌 단어의 개수
    
    for word in dat:
        seen = set()  # 등장한 문자 집합
        prev_char = None  # 이전 문자
        
        for char in word:
            if char != prev_char:
                if char in seen:  # 이미 등장한 문자라면 그룹 단어가 아님
                    cnt += 1
                    break
                seen.add(char)  # 등장한 문자 집합에 추가
            prev_char = char  # 이전 문자 갱신
    
    print(n-cnt)

if __name__ == "__main__":
    main()
