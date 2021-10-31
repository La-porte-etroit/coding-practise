num = int(input())
input_list = []

for i in range(num):
    a = input()
    input_list.append(a)

check = input_list.copy()

for word in input_list:
    word_list = list(word)
    alp_list = []
    for i in range(len(word_list)):
        if i == 0:
            alp_list.append(word_list[i])
        else:
            if word_list[i] == word_list[i-1]:
                pass
            else:
                if word_list[i] in alp_list:
                    check.remove(word)
                    break
                else:
                    alp_list.append(word_list[i])

print(len(check))