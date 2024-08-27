import sys
def main():
    input = sys.stdin.read
    data = input().strip().split()
    N = int(data[0])
    
    card = deque(data[1:])
    card_dequeue = []
    ind = 0
    while True:
        if not len(card):
            break
        card_dequeue.append(card.pop([ind]))
        ind += card_dequeue[-1] 

    sys.stdout.write(" ".join(card_dequeue) + " ")

if __name__ == "__main__":
    main()


