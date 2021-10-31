k = int(input())
data = []

for i in range(k):
    h, w, n = map(int, input().split())
    hwn = []
    hwn.extend([h, w, n])
    data.append(hwn)

for hwn in data:
    rooms = [[0 for col in range(hwn[0])] for row in range(hwn[1])]
    ans = []
    m = 1
    for row in rooms:
        n = 1
        for i in range(len(row)):
            if m < 10:
                row[i] = f'{n}0{m}'
            else:
                row[i] = f'{n}{m}'
            n += 1
        m += 1
        ans.extend(row)
    print(ans[hwn[2]-1])