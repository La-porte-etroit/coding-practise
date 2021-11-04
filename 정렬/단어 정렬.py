# 백준 1181번 <단어 정렬>
# 문제 출처: https://www.acmicpc.net/problem/1181

import sys

n = int(sys.stdin.readline())
l = []
for _ in range(n):
    a = input()
    if a not in l:
        l.append(a)

l.sort(key = lambda x: (len(x), x))  # 길이 순서대로 정렬, 길이가 같으면 알파벳 순으로 정렬
for i in l:
    print(i)