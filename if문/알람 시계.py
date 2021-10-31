h, m = map(int, input().split())

if 0 <= m <= 44:
    m += 15
    if 1 <= h <= 23:
        h -= 1
    else:
        h = 23
elif 45 <= m <= 59:
    m -= 45

print(h, m)