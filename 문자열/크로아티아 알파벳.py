a = input()
num = 0

for w in range(len(a)):
    if a[w] == '=':
        if a[w-1] == 'z' and a[w-2] == 'd':
            num -= 1
            pass
        elif a[w-1] == 'c' or a[w-1] == 's' or a[w-1] == 'z':
            pass
    elif a[w] == '-':
        if a[w-1] == 'c' or a[w-1] == 'd':
            pass
    elif a[w] == 'j':
        if a[w-1] == 'l' or a[w-1] == 'n':
            pass
        else:
            num += 1
    else:
        num += 1

print(num)