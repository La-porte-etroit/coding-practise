word = input()
word_list = list(word)

upper_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
lower_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
freq_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for a in word_list:
    if a in upper_list:
        freq_list[upper_list.index(a)] += 1
    else:
        freq_list[lower_list.index(a)] += 1

ans_list = []
for i in range(len(freq_list)):
    if freq_list[i] == max(freq_list):
        ans_list.append(upper_list[i])

if len(ans_list) >= 2:
    print('?')
else:
    print(ans_list[0])