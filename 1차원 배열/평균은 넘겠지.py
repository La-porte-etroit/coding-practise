N = int(input())
arr = []

for i in range(N):
    arr.append(input().split())

for row in arr:
    avr = 0
    n = 0
    for i in range(len(row)-1):
        avr += int(row[i+1])
    avr = avr/int(row[0])
    for i in range(len(row)-1):
        if int(row[i+1]) > avr:
            n += 1
    print('{:.3f}%'.format(n/int(row[0])*100))