import sys
from collections import deque

class Deck:
    def __init__(self):
        self.deck = deque()

    def f_enqueue(self, n):
        """덱 자료구조 맨 처음에 정수를 입력하는 함수"""
        self.deck.appendleft(n)

    def l_enqueue(self, n):
        """덱 자료구조 맨 마지막에 정수를 입력하는 함수"""
        self.deck.append(n)

    def f_dequeue(self):
        """덱 자료구조 맨 처음에 정수가 있다면 반환하고 삭제하는 함수"""
        if self.deck:
            return self.deck.popleft()
        else:
            return -1

    def l_dequeue(self):
        """덱 자료구조 맨 마지막에 정수가 있다면 반환하고 삭제하는 함수"""
        if self.deck:
            return self.deck.pop()
        else:
            return -1

    def front(self):
        """덱 자료구조 정수가 있다면 맨 처음 정수를 반환하는 함수"""
        if self.deck:
            return self.deck[0]
        else:
            return -1

    def back(self):
        """덱 자료구조 정수가 있다면 맨 마지막 정수를 반환하는 함수"""
        if self.deck:
            return self.deck[-1]
        else:
            return -1

    def is_empty(self):
        """덱 자료구조 정수가 있는지 없는지 확인.
        있다면 1을 없다면 0을 반환"""
        return 1 if not self.deck else 0

    def size(self):
        """덱 자료구조 사이즈를 정수로 반환"""
        return len(self.deck)

def main():
    input = sys.stdin.read
    data = input().strip().split('\n')
    N = int(data[0])
    commands = data[1:]

    my_deck = Deck()
    re_turn = []

    for command in commands:
        line = list(map(int, command.split()))
        cmd = line[0]

        if cmd == 1:
            n = line[1]
            my_deck.f_enqueue(n)
        elif cmd == 2:
            n = line[1]
            my_deck.l_enqueue(n)
        elif cmd == 3:
            re_turn.append(str(my_deck.f_dequeue()))
        elif cmd == 4:
            re_turn.append(str(my_deck.l_dequeue()))
        elif cmd == 5:
            re_turn.append(str(my_deck.size()))
        elif cmd == 6:
            re_turn.append(str(my_deck.is_empty()))
        elif cmd == 7:
            re_turn.append(str(my_deck.front()))
        elif cmd == 8:
            re_turn.append(str(my_deck.back()))

    sys.stdout.write("\n".join(re_turn) + "\n")

if __name__ == "__main__":
    main()
