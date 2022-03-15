# 백준 10866번 <덱>
# 문제 출처: https://www.acmicpc.net/problem/10866

# 해결한 방법
# 리스트를 이용해 덱을 구현하여 명령어에 따라 알맞게 코딩하였다.


import sys

N = int(sys.stdin.readline())
deque = []
for _ in range(N):
    command = sys.stdin.readline().split()
    if command[0] == 'push_front':
        deque.insert(0, command[1])
    elif command[0] == 'push_back':
        deque.append(command[1])
    elif command[0] == 'pop_front':
        if deque: print(deque.pop(0))
        else: print(-1)
    elif command[0] == 'pop_back':
        if deque: print(deque.pop())
        else: print(-1)
    elif command[0] == 'size':
        print(len(deque))
    elif command[0] == 'empty':
        if len(deque) == 0: print(1)
        else: print(0)
    elif command[0] == 'front':
        if deque: print(deque[0])
        else: print(-1)
    elif command[0] == 'back':
        if deque: print(deque[-1])
        else: print(-1)