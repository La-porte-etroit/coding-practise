n = int(input())

def ssum(a):
    k = 0
    for i in range(a+1):
        k += i
    return k

i = 0
while True:
    if n == 1:
        print('1')
        break
    elif 1 + 6*ssum(i) + 1 <= n <= 1 + 6*ssum(i+1):
        print(i+2)
        break
    else:
        i += 1