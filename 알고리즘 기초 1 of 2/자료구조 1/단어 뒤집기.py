# 백준 9093번 <단어 뒤집기>
# 문제 출처: https://www.acmicpc.net/problem/9093

# 해결한 방법
# 주어진 숫자만큼 for문을 돌려서 input의 문장을 split한 후 list로 변환해 주고,
# list의 원소, 즉 단어 하나를 for문으로 하나씩 가져와서 단어의 list를 만든 다음
# list의 길이가 0이 될 때까지 pop을 통해 계속해서 마지막 원소를 출력하게끔 하였다.


import sys

T = int(sys.stdin.readline())
for _ in range(T):
    s = list(sys.stdin.readline().split())
    for w in s:
        w_list = list(w)
        while len(w_list) != 0:
            print(w_list.pop(), end = '')
        print(' ', end = '')
    print()