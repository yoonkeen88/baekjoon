def main():
    data = []
    n = int(input())
    for i in range(n):
        a = input()
        if a not in data:
            data.append(a)

    data.sort( key=lambda x : (len(x), x) )       # 데이터를 정렬합니다.
    
    for i in data:
        print(i)

if __name__ == "__main__":
    main()