import sys
def combi(n, r):
    """Calculating the binominal coefficient when in n, r"""
    np = 1
    rp = 1
    for i in range(r):
        np *= (n-i)
        rp *= (i+1)
    result = np//rp
    return result  

def main():
    N = int(input())
    out = []
    for i in range(N):
        s,n = map(int, input().split())
        if s > n-s :
            out.append(combi(n,n-s))
        else:
            out.append(combi(n, s))
            
    for i in range(N):
        print(out[i])

if __name__ == "__main__":
    main()
