# 백준 17413번 <단어 뒤집기 2>
# 문제 출처: https://www.acmicpc.net/problem/17413

# 해결한 방법
# 주어진 문자열을 공백을 기준으로 'chunk'로 나누어 'L'이라는 리스트로 만들고, L에서 for문을 돌려 chunk를 하나씩 받아온다.
# a = True를 선언했는데, 이것은 chunk에 '<'나 '>'가 없을 때 그 chunk를 뒤집을지의 여부를 판단하는 변수이다.
# 
# 'N'이라는 리스트를 만들어 chunk에 대해 for문을 돌려서 '<'이나 '>'가 있을 때마다 그 인덱스를 N에 저장한다.
# 또한 for문 하나가 끝날 때마다 결과를 'chunk_list'에 넣어 준다.
# 
# N에 원소가 있을 때에는 첫 번째 원소가 '<'일 때, N의 길이가 1이라면 '<'만 있는 것이므로 chunk에서 '<'의 왼쪽에 원소가 있다면 그 문자열을 뒤집는다.
# 그리고 '<'의 오른쪽 원소들 및 다음 chunk는 '>'가 나오기 전까지는 뒤집히면 안 되므로 a = True를 입력해 준다.
# N의 길이가 2라면 '<'와 '>'가 있는 것이므로 '<'의 왼쪽 원소, 그리고 '>'의 오른쪽 원소가 존재한다면 그 문자열을 뒤집는다.
# 다음 chunk 역시 '<'가 나오기 전까지는 뒤집어야 하므로 a = False를 입력해 준다.
# N의 길이가 3 이상일 때는 '>'와 '<' 사이의 문자열은 뒤집어 주고, 나머지 경우의 수는 위의 N의 길이가 1일 때와 2일 때와 동일하게 처리한다.
# N의 첫 번째 원소가 '>'일 때도 마찬가지로 경우의 수를 나누어 처리한다.
# 
# N에 원소가 없을 때에는 우선 chunk_list에 원소가 있는지부터 확인해서 없다면 뒤집어야 하므로 뒤집는다.
# chunk_list에 원소가 있다면 a = True라면 pass하고 그렇지 않다면 문자열을 뒤집는다.
# 
# for문이 모두 끝나면 chunk_list의 원소들을 합친 후 그것으로 'final_chunk'라는 리스트를 만든다.
# 처음 사용자의 입력한 문자열의 리스트 'M'과 final_chunk의 원소를 하나하나 비교해서 'M'의 원소가 공백이 아닌 경우에 'M'의 원소를
# 'final_chunk'의 원소로 바꾸어 준다.


import sys

M = sys.stdin.readline().strip()
L = M.split()
chunk_list = []
a = True

for chunk in L:
    N = []
    for i in range(len(chunk)):
        if chunk[i] == '<' or chunk[i] == '>': N.append(i)
    if N:
        if chunk[N[0]] == '<':
            if len(N) == 1:
                if N[0] != 0:  # '<'가 첫 번째 원소가 아닌 경우
                    chunk = ''.join(reversed(list(chunk[:N[0]]))) + chunk[N[0]:]
                a = True
            elif len(N) == 2:
                if N[0] != 0:
                    chunk = ''.join(reversed(list(chunk[:N[0]]))) + chunk[N[0]:]
                    a = False
                if N[1] != len(chunk)-1:  # '>'가 마지막 원소가 아닌 경우
                    chunk = chunk[:N[1]+1] + ''.join(reversed(list(chunk[N[1]+1:])))
                    a = False
            else:
                if len(N)%2 == 0:
                    if N[0] != 0:
                        chunk = ''.join(reversed(list(chunk[:N[0]]))) + chunk[N[0]:]
                    if N[-1] != len(chunk)-1:
                        chunk = chunk[:N[-1]+1] + ''.join(reversed(list(chunk[N[-1]+1:])))
                    for i in range(2, len(N), 2):
                        if N[i] - N[i-1] != 1:  # '>'와 '<' 사이에 원소가 존재하는 경우
                            chunk = chunk[:N[i-1]+1] + ''.join(reversed(list(chunk[N[i-1]+1:N[i]]))) + chunk[N[i]:]
                    a = False
                else:
                    if N[0] != 0:
                        chunk = ''.join(reversed(list(chunk[:N[0]]))) + chunk[N[0]:]
                    for i in range(2, len(N), 2):
                        if N[i] - N[i-1] != 1:
                            chunk = chunk[:N[i-1]+1] + ''.join(reversed(list(chunk[N[i-1]+1:N[i]]))) + chunk[N[i]:]
                    a = True
        elif chunk[N[0]] == '>':
            if len(N) == 1:
                if N[0] != len(chunk)-1:
                    chunk = chunk[:N[0]+1] + ''.join(reversed(list(chunk[N[0]+1:])))
                a = False
            else:
                if len(N)%2 == 0:
                    for i in range(1, len(N), 2):
                        if N[i] - N[i-1] != 1:
                            chunk = chunk[:N[i-1]+1] + ''.join(reversed(list(chunk[N[i-1]+1:N[i]]))) + chunk[N[i]:]
                    a = True
                else:
                    if N[-1] != len(chunk)-1:
                        chunk = chunk[:N[-1]+1] + ''.join(reversed(list(chunk[N[-1]+1:])))
                    for i in range(1, len(N), 2):
                        if N[i] - N[i-1] != 1:
                            chunk = chunk[:N[i-1]+1] + ''.join(reversed(list(chunk[N[i-1]+1:N[i]]))) + chunk[N[i]:]
                    a = False
    else:
        if not chunk_list:
            chunk = chunk[::-1]
            a = False
        elif a == True:
            pass
        else:
            chunk = chunk[::-1]
    chunk_list.append(chunk)

M = list(M)
final_chunk = list(''.join(chunk_list))
c = 0  # final_chunk의 인덱스를 나타내는 변수로써, M에 final_chunk의 원소를 넣어 줄 때만 값이 1씩 증가함
for i in range(len(M)):
    if M[i] == ' ':  # input 문자열에 공백이 있을 경우 결과에도 똑같이 공백이 있어야 하므로 continue 해 줌
        continue
    else:
        M[i] = final_chunk[c]
        c += 1

print(''.join(M))