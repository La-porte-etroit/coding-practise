i = 1
result_list = []

while i <= 10000:
    i_list = list(str(i))
    result = 0
    for n in range(len(i_list)):
        result += int(i_list[n])
        result += int(i_list[n]) * pow(10, len(i_list) - 1 - n)
    result_list.append(result)
    if i not in result_list:
        print(i)
    i += 1