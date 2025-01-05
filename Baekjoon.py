def main():
    n = int(input())
    facto = 1
    for i in range(1, n+1):
        facto *= i
  
    l = len(str(facto))
    cnt =0 
    for x in range(l, 0, -1):
        if str(facto)[x-1] =='0' : 
           cnt +=1
        else:
            break
    print(cnt) 



if __name__ == "__main__":
    main()