N, M = map(int, input().split())
l = list(map(int, input().split()))
s = []

for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            if l[i] + l[j] + l[k] <= M:
                s.append(l[i] + l[j] + l[k])

print(max(s))