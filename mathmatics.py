def sieve_of_eratosthenes(m, n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False 

    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    primes = [i for i in range(m, n + 1) if is_prime[i]]
    return primes


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
    
def josephus_sequence(N, K):
    circle = list(range(1, N + 1))  # 1부터 N까지의 숫자를 원형으로 저장
    result = []

    index = 0
    while circle:
        index = (index + K - 1) % len(circle)  # K번째 사람을 찾기 위한 인덱스 계산
        result.append(circle.pop(index))       # 해당 사람을 제거하고 결과에 추가

    return result