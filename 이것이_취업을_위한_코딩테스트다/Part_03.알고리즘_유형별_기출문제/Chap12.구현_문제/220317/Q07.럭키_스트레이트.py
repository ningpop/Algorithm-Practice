# 2022.03.17
# 제한 시간 20분 / 풀이 시간 7분 10초
# 채점 결과: 정답
# 시간복잡도: O(N)..?
# 문제 링크: https://www.acmicpc.net/problem/18406

n = input()

mid = len(n) // 2
left = n[:mid]
right = n[mid:]

if sum(map(int, list(left))) == sum(map(int, list(right))):
    print('LUCKY')
else:
    print("READY")