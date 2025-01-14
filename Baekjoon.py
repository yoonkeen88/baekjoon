import sys
def main():
    h,m = map(int,sys.stdin.readline().strip().split())
    m -= 45
    if m <0:
        if h-1 <0:
            print(f'{24-1} {60 +m}')
        else:
            print(f"{h-1} {60+m}")
    else:
        print(print(f"{h} {m}"))
    
if __name__ == "__main__":
    main()