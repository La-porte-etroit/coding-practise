a = input()
ans = 0
a_list = list(a)
space_idx = []

for i in range(len(a_list)):
    if a_list[i] == ' ':
        space_idx.append(i)

for i in space_idx:
    if i == 0:
        pass
    elif i == len(a_list) - 1:
        pass
    else:
        if a_list[i - 1] != ' ' and a_list[i + 1] != ' ':
            ans += 1

if ans != 0:
    print(ans + 1)
else:
    for i in a_list:
        if i != ' ':
            ans = 1
            break
    print(ans)