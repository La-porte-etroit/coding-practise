N = int(input())
a = 1

def fact(n):
    global a
    if n == 0:
        pass
    else:
        a *= n
        fact(n-1)

if N == 0:
    print(1)
else:
    fact(N)
    print(a)