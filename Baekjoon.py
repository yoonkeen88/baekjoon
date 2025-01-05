def fibo_recursion(number: int) -> int:
    """
    fibonacci function by recursion.
    :param number: integer number
    :return: integer number
    """
    if number == 0:
        return 0
    elif number == 1:
        return 1
    else:
        return fibo_recursion(number - 1) + fibo_recursion(number - 2)




def main():
    N = int(input())  # 카드의 개수 입력 받기
    print(fibo_recursion(N))


if __name__ == "__main__":
    main()
