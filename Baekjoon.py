import sys

def main():
    answer = []
    while True:
        try:
            a = list(map(int, input().split()))
        except ValueError:
            print("숫자 세 개를 입력하세요.")
            continue
        if a == [0, 0, 0]: 
            break
        
        if len(a) != 3:  
            print("정확히 세 개의 숫자를 입력하세요.")
            continue
        
        a.sort()
        if a[0]**2 + a[1]**2 == a[2]**2:
            answer.append("right")
        else:
            answer.append("wrong")

    sys.stdout.write("\n".join(answer) + "\n")

if __name__ == "__main__":
    main()
