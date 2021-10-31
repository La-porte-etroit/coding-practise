num = int(input())
input_list = []
for i in range(num):
    a = input()
    input_list.append(a)

for a in input_list:
    a_list = list(a)
    num = int(a_list[0])
    for i in range(len(a_list) - 2):
        for j in range(num):
            if i == len(a_list) - 3 and j == num - 1:
                print(a_list[i + 2])
            else:
                print(a_list[i + 2], end = '')