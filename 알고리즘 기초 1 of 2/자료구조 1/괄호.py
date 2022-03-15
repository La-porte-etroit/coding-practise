# 백준 9012번 <괄호>
# 문제 출처: https://www.acmicpc.net/problem/9012

# 해결한 방법
# 주어진 숫자만큼 for문을 돌려서 괄호 input을 입력받아 list로 변환해 주고, count라는 변수를 선언한다.
# list에 대해 for문을 돌려서 원소가 '('이면 count에 1을 더하고, ')'이면 count에서 1을 뺀다.
# 'NO'가 출력되는 조건은 count가 0보다 작을 때, 그리고 for문을 다 돌았는데 count가 0이 아닐 때이다.
# count가 0보다 작은 경우는 '('보다 ')'가 더 많이 등장했을 때이고,
# for문을 다 돌았는데 count가 0이 아닌 경우는 '('가 ')'보다 더 많을 때이다.


import sys

T = int(sys.stdin.readline())
for _ in range(T):
    P = list(input())
    count = 0
    for i in range(len(P)):
        if P[i] == '(':
            count += 1
        else:
            count -= 1
            if count < 0:
                print('NO')
                break
        if i == len(P)-1:
            if count == 0:
                print('YES')
            else:
                print('NO')