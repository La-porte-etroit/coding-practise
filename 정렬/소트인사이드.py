# 백준 1427번 <소트인사이드>
# 문제 출처: https://www.acmicpc.net/problem/1427

import sys

n = list(sys.stdin.readline())
n.sort(reverse = True)
for i in n:
    print(i, end = '')