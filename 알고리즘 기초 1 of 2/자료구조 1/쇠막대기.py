# 백준 10799번 <쇠막대기>
# 문제 출처: https://www.acmicpc.net/problem/10799

# 해결한 방법
# 쇠막대기의 갯수를 나타내는 변수 'count'를 1로, 정답을 나타내는 변수 'ans'를 0으로 초기화해 준다.
# 괄호를 받아와서 인덱스 1부터 for문을 돌린다. 인덱스 0은 무조건 '('이고, 인덱스 1이 만약에 '('라면 앞의 '('는 쇠막대기임이 확실하고,
# 이 인덱스의 괄호는 쇠막대기일 수도 있고 아닐 수도 있지만, 우선 count에 1을 더해 준다.
# 예를 들어 인덱스 2가 ')'라면 앞의 '('는 레이저이므로 다시 count에서 1을 빼 주고, 현재까지의 count가 쇠막대기의 갯수이므로 레이저에 의해
# count개의 조각이 생긴다. 따라서 count를 ans에 더해 준다.
# 만약에 ')'가 나왔는데 앞의 괄호도 ')'였다면 이 괄호는 쇠막대기의 끝을 의미하므로 이 끄트머리 조각 1을 ans에 더해 주고 count에서 1을 뺀다.


import sys

P = sys.stdin.readline().rstrip()
count = 1
ans = 0
for i in range(1, len(P)):
    if P[i] == '(': count += 1
    else:
        count -= 1
        if P[i-1] == '(': ans += count
        else: ans += 1
print(ans)