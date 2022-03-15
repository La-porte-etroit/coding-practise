# 백준 1158번 <요세푸스 문제>
# 문제 출처: https://www.acmicpc.net/problem/1158

# 해결한 방법
# num이라는 변수를 지정해서 K-1만큼 더해가며 N만큼의 수가 들어있는 리스트에서 해당 인덱스의 원소를 제거해 answer라는 리스트에 추가하고,
# num이 리스트의 길이 이상이 될 경우 그것을 리스트의 길이로 나눈 나머지로 초기화한다.


import sys

N, K = map(int, sys.stdin.readline().split())
l = [i for i in range(1, N+1)]
answer = []
num = 0

for _ in range(N):
    num += K-1
    if num >= len(l):
        num = num % len(l)
    answer.append(str(l.pop(num)))

print('<', ', '.join(answer)[:], '>', sep = '')