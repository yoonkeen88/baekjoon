def josephus_sequence(N, K):
    circle = list(range(1, N + 1))  # 1부터 N까지의 숫자를 원형으로 저장
    result = []

    index = 0
    while circle:
        index = (index + K - 1) % len(circle)  # K번째 사람을 찾기 위한 인덱스 계산
        result.append(circle.pop(index))       # 해당 사람을 제거하고 결과에 추가

    return result

# 입력 받기
N, K = map(int, input().split())

result = josephus_sequence(N, K)

# 결과를 원하는 형식으로 변환하여 출력
result_str = '<' + ', '.join(map(str, result)) + '>'
print(result_str)  # sys.stdout.write 대신 print 사용
