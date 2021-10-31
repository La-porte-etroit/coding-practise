T = int(input())
arr = []
for _ in range(T):
    arr.append(list(map(int, input().split())))

def dis(x1, y1, x2, y2):
    return (abs(x1-x2)**2 + abs(y1-y2)**2)**0.5

for c in arr:
    d = dis(c[0], c[1], c[3], c[4])

    if c[0] == c[3] and c[1] == c[4]:
        if c[2] == c[5]:
            print(-1)
        else: print(0)
    else:
        if c[2] + c[5] < d:
            print(0)
        elif c[2] + c[5] == d:  
            print(1)
        else:
            if c[2] > d+c[5] or c[5] > d+c[2]:
                print(0)
            elif c[2] == d+c[5] or c[5] == d+c[2]:
                print(1)
            else:
                print(2)