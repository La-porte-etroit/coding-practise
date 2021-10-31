a = input()
a_rev = a[::-1]
s = a_rev.split()

num1 = int(s[0])
num2 = int(s[1])

if num1 > num2:
    print(num1)
else:
    print(num2)