'''
BOJ 18406
https://www.acmicpc.net/problem/18406
'''

import sys

N = str(sys.stdin.readline()) # 정수 입력

start = N[:len(N) // 2]
end = N[len(N) // 2:]

start_value = 0
end_value = 0
for i, j in zip(start, end):
    start_value += int(i)
    end_value += int(j)

if start_value == end_value:
    print('LUCKY')
else:
    print('READY')