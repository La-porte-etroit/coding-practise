# 백준 1406번 <에디터>
# 문제 출처: https://www.acmicpc.net/problem/1406

# 해결한 방법
# 처음에는 가장 하단의 '실패한 코드'처럼 커서의 위치를 숫자로 나타내는 cursor라는 변수를 지정해서 명령어에 따라 cursor에 숫자를 더하거나 빼고,
# remove와 insert를 이용하여 구현을 하였지만 시간 초과가 발생하여 연산 시간을 줄이기 위해 다른 방법을 사용하였다.
# 리스트를 두 개를 만들어서 처음에는 리스트 1에 모든 문자열을 집어넣고 리스트 2는 빈 상태로 존재한다.
# 명령어가 L일 때에는 리스트 1에서 pop한 것을 리스트 2에 집어넣고, D일 때에는 반대로 한다.
# 이 때 리스트 1과 2의 사이가 커서의 역할을 한다고 보면 된다.
# 따라서 명령어가 B일 때에는 리스트 1에 원소가 존재하면 pop을 하면 되고, 명령어가 P일 때에는 append를 하면 된다.


import sys

b1 = list(sys.stdin.readline().strip())
b2 = []
M = int(sys.stdin.readline())

for _ in range(M):
    command = sys.stdin.readline().split()
    if command[0] == 'L':
        if b1: b2.append(b1.pop())
        else: continue
    elif command[0] == 'D':
        if b2: b1.append(b2.pop())
        else: continue
    elif command[0] == 'B':
        if b1: b1.pop()
        else: continue
    elif command[0] == 'P':
        b1.append(command[1])

print(''.join(b1 + list(reversed(b2))))


# 실패한 코드

# import sys
# 
# body = list(sys.stdin.readline())
# body.pop()
# init = cursor = len(body)
# M = int(sys.stdin.readline())
# for i in range(M):
#     command = sys.stdin.readline().split()
#     if command[0] == 'L':
#         if cursor != 0:
#             cursor -= 1
#     if command[0] == 'D':
#         if cursor != init:
#             cursor += 1
#     if command[0] == 'B':
#         if cursor >= 1:
#             body.remove(body[cursor-1])
#             cursor -= 1
#     if command[0] == 'P':
#         body.insert(cursor, command[1])
#         cursor += 1

# for i in body:
#     print(i, end = '')