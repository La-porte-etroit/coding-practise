word = input()

alp_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
word_list = list(word)

for alp in alp_list:
    if alp in word_list:
        print(word_list.index(alp), end = ' ')
    else:
        print('-1', end = ' ')