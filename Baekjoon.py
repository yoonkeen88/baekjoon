def main():
    n = int(input())
    cnt = 0
    defal = 666 # 666 이 들어가는 N 번째로 큰수를 찾아야함
    
    while cnt < n:
        if "666" in str(defal):
            cnt += 1
        defal += 1
    print(defal-1)


if __name__ == "__main__":
    main()