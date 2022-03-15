# 백준 10845번 <큐>
# 문제 출처: https://www.acmicpc.net/problem/10845

# 해결한 방법
# 정수를 저장할 큐의 역할을 할 리스트를 만든 다음 명령어에 따라 알맞게 코딩하였다.


import sys

N = int(sys.stdin.readline())
queue = []
n = 0
for _ in range(N):
    command = sys.stdin.readline().split()
    if command[0] == 'push':
        queue.append(command[1])
        n += 1
    elif command[0] == 'pop':
        if n == 0: print(-1)
        else:
            print(queue.pop(0))
            n -= 1
    elif command[0] == 'size':
        print(n)
    elif command[0] == 'empty':
        if n == 0: print(1)
        else: print(0)
    elif command[0] == 'front':
        if n == 0: print(-1)
        else: print(queue[0])
    elif command[0] == 'back':
        if n == 0: print(-1)
        else: print(queue[n-1])