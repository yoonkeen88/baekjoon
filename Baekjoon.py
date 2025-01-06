import sys

def fibo_recursion(number: int) -> int:
    """
    Fibonacci function using recursion.
    Tracks the number of times 0 and 1 are returned.
    :param number: integer number
    :return: integer number
    """
    global zero
    global one

    if number == 0:
        zero += 1
        return 0
    elif number == 1:
        one += 1
        return 1
    else:
        return fibo_recursion(number - 1) + fibo_recursion(number - 2)

def main():
    global zero, one

    n = int(sys.stdin.readline().strip())
    for _ in range(n):
        zero = 0
        one = 0
        number = int(sys.stdin.readline().strip())
        fibo_recursion(number)
        print(zero, one)

if __name__ == "__main__":
    main()
