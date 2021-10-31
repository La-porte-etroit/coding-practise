m, n, d = map(int, input().split())

a = (d-m)/(m-n)
if float(a) == int(a):
    print(int(a+1))
else:
    print(int(a+2))