import sys
from collections import defaultdict, deque

def bfs(graph,visit):
    """
    
    """
def main():
    
    t = int(sys.stdin.readline().strip())
    result = []
    for _ in range(t):
        graph = defaultdict(list)
        m,n,k = map(int,sys.stdin.readline().strip().split())
        for _ in range(k):
            i,j = map(int,sys.stdin.readline().strip().split())
            graph[i].append(j)
            graph[j].append(i)
        
        

if __name__ == "__main__":
    main()
