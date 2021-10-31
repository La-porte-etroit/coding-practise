def f(n):
    global arr

    if n == 3:
        arr[0][:3] = arr[2][:3] = [1]*3
        arr[1][:3] = [1, 0, 1]
        return
    
    f(n//3)

    for i in range(n//3):
        for j in range(n//3):
            for k in range(3):
                for l in range(3):
                    arr[i+(n//3)*k][j+(n//3)*l] = arr[i][j]
    for i in range(n//3):
        for j in range(n//3):
            arr[n//3+i][n//3+j] = 0


N = int(input())

arr = [[0 for row in range(N)] for col in range(N)]

f(N)

for i in arr:
    for j in i:
        if j == 1:
            print('*', end = '')
        else:
            print(' ', end = '')
    print()