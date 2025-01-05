def main():
    n = int(input())
    li = input().split()
    t, p = map(int,input().split())
    
    t_or = 0
    for i in range(len(li)): 
        num = int(li[i])
        if num ==0:
            continue
        else:
            if num% t == 0:
                t_or += num//t
            else:
                t_or += num//t + 1
        
    print(f"{t_or}\n{n//p} {n%p}")
if __name__ == "__main__":
    main()