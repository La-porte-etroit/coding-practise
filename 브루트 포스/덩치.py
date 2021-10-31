N = int(input())
L = []
r = [0 for i in range(N)]
for i in range(N):
    L.append(list(map(int, input().split())))

for i in range(N):
    rank = 1
    for j in range(N):
        if i != j and L[j][0] > L[i][0] and L[j][1] > L[i][1]:
            rank += 1
    r[i] = rank

for i in r:
    print(i, end = ' ')