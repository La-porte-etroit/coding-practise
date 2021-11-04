# 백준 10814번 <나이순 정렬>
# 문제 출처: https://www.acmicpc.net/problem/10814

import sys

n = int(sys.stdin.readline())
l = []
for i in range(n):
    l.append(list(sys.stdin.readline().split()))

l.sort(key = lambda x: int(x[0]))  # lambda 함수를 사용하여 나이순으로 먼저 정렬, 나이가 같다면 자동으로 입력순으로 정렬됨
for i in l:
    print(i[0], i[1])