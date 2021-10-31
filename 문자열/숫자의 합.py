a = int(input())
b = input()
b_list = list(b)
sum = 0

for i in range(a):
    sum += int(b_list[i])

print(sum)