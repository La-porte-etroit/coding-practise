# 백준 11650번 <좌표 정렬하기>
# 문제 출처: https://www.acmicpc.net/problem/11650

import sys

n = int(sys.stdin.readline())
l = []
for _ in range(n):
    l.append(list(map(int, sys.stdin.readline().split())))

l.sort(key = lambda x: (x[0], x[1]))  # x좌표, y좌표 순으로 정렬
for i in l:
    print(i[0], i[1])