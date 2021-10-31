# 백준 2108번 <통계학>
# 문제 출처: https://www.acmicpc.net/problem/2108

import sys

n = int(sys.stdin.readline())
l = [0]*n
for i in range(n):
    l[i] = int(sys.stdin.readline())


# 산술평균
s = 0
for i in l:
    s += i
print(round(s/n))


# 중앙값
l.sort()
print(l[int((n-1)/2)])


# 최빈값
# 리스트 l의 각 원소의 빈도수를 구할 때 처음에는 count를 사용하였는데, count를 사용하게 되면 원소 하나의 빈도수를 구할 때마다 리스트의 모든 원소를 다 확인하기 때문에 모든 원소의 빈도수를 구하려면 시간이 오래 걸린다. 따라서 아래와 같은 방법으로 최빈값을 구했다.
f = {}

# 아래와 같이 리스트 l을 한 번만 확인하여 모든 원소의 빈도수를 구할 수 있다.
for i in l:
    if i not in f:
        f[i] = 1
    else:
        f[i] += 1

f_keys = list(f.keys())
f_values = list(f.values())

# f에서 최빈값을 가지는 key값만을 뽑는 과정
a = []
for i in range(len(f_values)):
    if f_values[i] == max(f_values):
        a.append(f_keys[i])

if len(a) > 1:
    print(a[1])
else:
    print(a[0])


# 범위
print(max(l)-min(l))