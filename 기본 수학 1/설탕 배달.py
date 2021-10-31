N = int(input())

s = N//5

while s >= 0:
    if (N - 5*s)%3 == 0:
        print(s + (N - 5*s)//3)
        break
    else:
        if s > 0:
            s -= 1
        else:
            print('-1')
            break