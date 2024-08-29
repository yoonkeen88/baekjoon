def mainn():
    N = int(input())  # 카드의 개수 입력 받기
    cards = list(map(int, input().split()))  # 카드 값 입력 받기
    balloons = list(range(N))  # 카드 위치를 나타내는 리스트 생성
    ind = 0  # 현재 인덱스

    result = []

    while cards:
        result.append(balloons.pop(ind)+1)  # 해당 카드의 원래 위치 기록
        mov = cards.pop(ind)
        
        if cards:  
            ind = (ind + mov) % len(balloons)
            print(ind)  
       
    print(" ".join(map(str, result)))  # 결과 출력
def main():
    print(-1%3)

if __name__ == "__main__":
    main()
