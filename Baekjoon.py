import sys

class Circular:
    def __init__(self, n):
        self.circular = list(range(1, n + 1))
        
    def peek(self, ind):
        result = []
        index = ind - 1  # 0-based index
        
        while self.circular:
            index = index % len(self.circular)
            result.append(self.circular.pop(index))
            
        return result

def main():
    t = list(map(int, sys.stdin.readline().strip().split()))
    n, k = t[0], t[1]
    
    my_ls = Circular(n)
    result = my_ls.peek(k)
    

    result_str = '<' + ', '.join(map(str, result)) + '>'
    sys.stdout.write(result_str + "\n")

if __name__ == "__main__":
    main()
