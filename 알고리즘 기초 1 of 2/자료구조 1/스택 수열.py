# 백준 1874번 <스택 수열>
# 문제 출처: https://www.acmicpc.net/problem/1874

# 해결한 방법
# 입력된 수열의 리스트, 1부터 n까지의 수가 들어올 스택(리스트), '+'와 '-'가 들어갈 정답 리스트를 선언한다.
# 스택이 비어 있으면 맨 처음에는 1, 처음이 아니라면 그 다음으로 들어와야 하는 수를 스택에 추가하며, 이와 동시에 정답 리스트에 '+'를 추가한다.
# 스택이 비어 있지 않고, 스택의 마지막 수와 수열 리스트의 첫 번째 수가 같다면 두 리스트에서 각각 그 수를 없애고 정답 리스트에 '-'를 추가한다.
# 이런 방식으로 수를 1씩 늘려가면서 진행하다가 수가 n이 되었을 때,
# 수열을 만들 수 있는 경우라면 두 리스트에서 수가 점점 줄어들다가 텅 비게 되어 while문을 빠져나오고,
# 수열을 만들 수 없는 경우라면 수가 n보다 커지게 되어 'NO'가 출력되고 while문이 break된다.


import sys

n = int(sys.stdin.readline())
L = []
for _ in range(n):
    L.append(int(sys.stdin.readline()))

l = []  # 스택
i = 1
answer = []
a = True
while True:
    if len(l) == 0:
        l.append(i)
        answer.append('+')
        i += 1
    else:
        if l[-1] == L[0]:
            l.pop()
            L.remove(L[0])
            answer.append('-')
        else:
            if i > n:
                print('NO')
                a = False  # 수열을 만들 수 없는 경우에는 'NO'만 출력해야 하므로
                break
            else:
                l.append(i)
                answer.append('+')
                i += 1
    if len(L) == 0:
        break

if a == True:
    for i in answer:
        print(i)