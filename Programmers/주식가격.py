from collections import deque

def solution(prices: list) -> list:
    total_time = len(prices)
    queue = deque(prices)
    answer = []
    
    for i in range(total_time):
        jusik = queue.popleft()
        time = 0
        for j in queue:
            time += 1
            if jusik > j:
                break
        answer.append(time)
    return answer

print(solution([1, 2, 3, 2, 3]))