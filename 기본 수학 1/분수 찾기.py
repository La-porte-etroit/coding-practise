n = int(input())

end = 1
plus = 2
l = 1

while n > end:
    l += 1
    end += plus
    plus += 1

if l%2 == 0:
    print(f'{(l+1)-(end-n+1)}/{end-n+1}')
else:
    print(f'{end-n+1}/{(l+1)-(end-n+1)}')