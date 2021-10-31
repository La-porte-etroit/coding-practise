a = int(input())
case = []

for i in range(a):
    arr = []
    k = int(input())
    n = int(input())
    arr.extend([k, n])
    case.append(arr)

for c in case:
    arr = [[0 for col in range(c[1])] for row in range(c[0]+1)]

    for i in range(c[0]+1):
        arr[i][0] = 1
    for i in range(c[1]):
        arr[0][i] = i+1

    for i in range(c[0]):
        i += 1
        for j in range(c[1]):
            j += 1
            if j == c[1]:
                break
            arr[i][j] = arr[i-1][j] + arr[i][j-1]

    print(arr[c[0]][c[1]-1])


'''
1 2 3  4  5     0층

1 3 6  10 15    1층
1 4 10 20 35    2층
1 5 15 35 70    3층
1 6 21 56 126   4층

'''

'''
1*1    1*4 + 2*1    1*10 + 2*4 + 3*1   1*20 + 2*10 + 3*4 + 4*1                            4층
1*1    1*3 + 2*1    1*6 + 2*3 + 3*1    1*10 + 2*6 + 3*3 + 4*1                             3층
1*1    1*2 + 2*1    1*3 + 2*2 + 3*1    1*4 + 2*3 + 3*2 + 4*1                              2층
1*1    1*1 + 2*1    1*1 + 2*1 + 3*1    1*1 + 2*1 + 3*1 + 4*1                              1층

1      2            3                  4                                                  0층
'''