# 백준 10828번 <스택>
# 문제 출처: https://www.acmicpc.net/problem/10828

# 해결한 방법
# 주어진 숫자만큼 for문을 돌려서 input으로 들어온 명령어에 따라 문제 조건에 맞는 명령을 수행하게 하였다.


import sys

N = int(sys.stdin.readline())
L = []
for _ in range(N):
    i = sys.stdin.readline().split()  # push가 들어올 경우를 대비해 split을 해 놓는다
    if i[0] == 'pop':
        if len(L) == 0:
            print(-1)
        else:
            print(L.pop())
    elif i[0] == 'size':
        print(len(L))
    elif i[0] == 'empty':
        if len(L) == 0:
            print(1)
        else:
            print(0)
    elif i[0] == 'top':
        if len(L) == 0:
            print(-1)
        else:
            print(L[-1])
    else:  # push가 들어온 경우. i[1]이 push 뒤의 숫자
        L.append(int(i[1]))