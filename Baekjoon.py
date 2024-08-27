import sys

def main():
    N = int(input())  
    cards = list(map(int, sys.stdin.read().strip().split()))  
    ind = 0
    result = [] 

    while cards:
        result.append(ind+1) 
        current_value = cards.pop(ind) 
        if cards: 
            if current_value + ind < 0:
                ind = (len(cards) + (current_value+ind +1))%len(cards)

            else:
                ind = (ind + current_value) % len(cards) 

    sys.stdout.write(" ".join(map(str, result)) + "\n")  

if __name__ == "__main__":
    main()



