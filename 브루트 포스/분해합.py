N = int(input())

for i in range(N):
    i += 1
    k = i
    if i == N:
        print(0)
    for j in str(k):
        k += int(j)
    if k == N:
        print(i)
        break