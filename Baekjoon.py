def main():
    a,b = map(int, input().split())

    if a < b:
        a,b = b,a
    mx = 1
    for i in range(b,0,-1):
        if a%i ==0 and b%i == 0:
            mx =i
            break
        else: 
            continue
    print(f"{mx}\n{a*b//mx}")

if __name__ == "__main__":
    main()