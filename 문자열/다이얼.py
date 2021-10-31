word = input()
time = 0
word_list = list(word)

for word in word_list:
    if word == 'A' or word == 'B' or word == 'C':
        time += 3
    elif word == 'D' or word == 'E' or word == 'F':
        time += 4
    elif word == 'G' or word == 'H' or word == 'I':
        time += 5
    elif word == 'J' or word == 'K' or word == 'L':
        time += 6
    elif word == 'M' or word == 'N' or word == 'O':
        time += 7
    elif word == 'P' or word == 'Q' or word == 'R' or word == 'S':
        time += 8
    elif word == 'T' or word == 'U' or word == 'V':
        time += 9
    elif word == 'W' or word == 'X' or word == 'Y' or word == 'Z':
        time += 10

print(time)