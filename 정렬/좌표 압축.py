# 백준 18870번 <좌표 압출>
# 문제 출처: https://www.acmicpc.net/problem/18870

import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
arr2 = sorted(list(set(arr)))  # arr에서 중복되는 원소를 없애기 위해 set 사용
dic = {arr2[i]: i for i in range(len(arr2))}  # dic에는 각 원소의 좌표 압축 결과값이 저장됨

for i in arr:
    print(dic[i], end = ' ')