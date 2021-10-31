M = int(input())
N = int(input())

ssum = 0
min = 0

for i in range(M, N+1):
    if i == 1:
        pass
    elif i == 2:
        ssum += i
        min = i
    else:
        for j in range(2, i):
            if i%j == 0:
                break
            if j == i-1:
                ssum += i
                if min == 0:
                    min = i

if ssum == 0:
    print(-1)
else:
    print(ssum)
    print(min)