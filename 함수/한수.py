num = int(input())
i = 1
hansoo_num = 0

while i <= num:
    i_list = list(str(i))
    if len(i_list) == 1 or len(i_list) == 2:
        hansoo_num += 1
        i += 1
    elif len(i_list) == 3:
        if int(i_list[0]) - int(i_list[1]) == int(i_list[1]) - int(i_list[2]):
            hansoo_num += 1
            i += 1
        else:
            i += 1
    else:
        for a in range(len(i_list) - 2):
            if int(i_list[a]) - int(i_list[a + 1]) == int(i_list[a + 1]) - int(i_list[a + 2]):
                decision = True
            else:
                decision = False
                break
        if decision == True:
            hansoo_num += 1
            i += 1
        else:
            i += 1

print(hansoo_num)