T = int(input())
arr = []

for _ in range(T):
    n = int(input())
    arr.append(n)

def sosu(n):
    for i in range(2, n+1):
        if n%i == 0:
            if n == i:
                return True
            else:
                return False

for n in arr:
    a = int(n/2)
    for i in range(a, 1, -1):
        if sosu(i) == True:
            if sosu(n-i) == True:
                print(i, n-i)
                break