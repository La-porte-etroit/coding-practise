def sosu(m):
    n = m*2
    m += 1
    
    prime = [True]*(n+1)
    prime[1] = False

    for i in range(2, int(n**0.5)+1):
        if prime[i] == True:
            for j in range(i*2, n+1, i):
                prime[j] = False

    k = 0
    for i in range(m, n+1):
        if prime[i] == True:
            k += 1
    
    print(k)

arr = []

while True:
    a = int(input())
    if a == 0: break
    else: arr.append(a)

for i in arr:
    sosu(i)