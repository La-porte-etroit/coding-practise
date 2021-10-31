n = int(input())
a = True

while a == True:
    if int(pow(n, 0.5)) >= 2:
        for i in range(2, int(pow(n, 0.5))+1):
            if n%i == 0:
                print(i)
                n = n/i
                break
            if i >= int(pow(n, 0.5)) and n%i != 0:
                a = False
    else:
        a = False

if n == 1:
    pass
else:
    print(int(n))