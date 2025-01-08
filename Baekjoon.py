from collections import deque

def printer_queue(test_cases):
    results = []
    for case in test_cases:
        n, m = case[0]
        priorities = case[1]
        
        # 큐 생성: (문서 중요도, 초기 인덱스)
        queue = deque((priority, idx) for idx, priority in enumerate(priorities))
        
        order = 0  # 인쇄 순서
        while queue:
            current = queue.popleft()
            
            # 현재 문서보다 중요도가 높은 문서가 있는지 확인
            if any(current[0] < item[0] for item in queue):
                queue.append(current)  # 뒤로 보냄
            else:
                order += 1  # 인쇄
                if current[1] == m:  # 목표 문서가 인쇄됨
                    results.append(order)
                    break
    return results

# 입력 처리
if __name__ == "__main__":
    t = int(input())  # 테스트케이스 수
    test_cases = []
    for _ in range(t):
        n, m = map(int, input().split())
        priorities = list(map(int, input().split()))
        test_cases.append(((n, m), priorities))
    
    # 결과 계산 및 출력
    results = printer_queue(test_cases)
    for res in results:
        print(res)
