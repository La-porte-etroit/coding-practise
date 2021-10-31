# 감시 피하기

# 사용자에게 복도 한 줄의 정보를 입력 받고 공백을 없앤 리스트의 형태로 반환
def make_row():
    row = list(input())
    for elm in row:
        if elm == ' ':
            row.remove(' ')
    return row

# 사용자에게 숫자와 숫자에 따른 복도의 정보를 입력받음
num = int(input())

if num == 3:
    row1 = make_row()
    row2 = make_row()
    row3 = make_row()
    arr = [[0 for col in range(3)] for row in range(3)]
    arr[0] = row1
    arr[1] = row2
    arr[2] = row3
elif num == 4:
    row1 = make_row()
    row2 = make_row()
    row3 = make_row()
    row4 = make_row()
    arr = [[0 for col in range(4)] for row in range(4)]
    arr[0] = row1
    arr[1] = row2
    arr[2] = row3
    arr[3] = row4
elif num == 5:
    row1 = make_row()
    row2 = make_row()
    row3 = make_row()
    row4 = make_row()
    row5 = make_row()
    arr = [[0 for col in range(5)] for row in range(5)]
    arr[0] = row1
    arr[1] = row2
    arr[2] = row3
    arr[3] = row4
    arr[4] = row5
elif num == 6:
    row1 = make_row()
    row2 = make_row()
    row3 = make_row()
    row4 = make_row()
    row5 = make_row()
    row6 = make_row()
    arr = [[0 for col in range(6)] for row in range(6)]
    arr[0] = row1
    arr[1] = row2
    arr[2] = row3
    arr[3] = row4
    arr[4] = row5
    arr[5] = row6

# 선생님, 학생, 장애물의 좌표 값을 저장할 딕셔너리
teacher = dict()
student = dict()
obstacle = dict()

# 선생님, 학생, 장애물의 수
tnum = 1
snum = 1
obnum = 1

# 선생님과 학생의 좌표 값을 생성
i = 0
for row in arr:
    j = 0
    for elm in row:
        if elm == 'T':
            teacher[f'T{tnum}'] = i, j
            tnum += 1
            j += 1
        elif elm == 'S':
            student[f'S{snum}'] = i, j
            snum += 1
            j += 1
        else:
            j += 1
    i += 1

tlist = list(teacher.values())
slist = list(student.values())

# 장애물의 좌표 값을 생성
# 행 혹은 열이 같은 선생님-학생 짝을 생성하고, 둘 사이의 좌표들이 장애물의 위치이므로 그 좌표들을 딕셔너리에 저장
for t in tlist:
    for s in slist:
        if t[0] == s[0]:
            oblist = []
            for i in range(abs(t[1] - s[1]) - 1):
                if t[1] > s[1]:
                    if (t[0], s[1] + i + 1) not in tlist:
                        oblist.append((t[0], s[1] + i + 1))
                elif s[1] > t[1]:
                    if (t[0], t[1] + i + 1) not in tlist:
                        oblist.append((t[0], t[1] + i + 1))
            oblist_copy = oblist.copy()
            for ob in oblist_copy:
                if ob in slist:
                    oblist_copy.remove(ob)
            if oblist == oblist_copy:
                obstacle[f'Ob{obnum}'] = oblist
                obnum += 1
        elif t[1] == s[1]:
            oblist = []
            for i in range(abs(t[0] - s[0]) - 1):
                if t[0] > s[0]:
                    if (s[0] + i + 1, t[1]) not in tlist:
                        oblist.append((s[0] + i + 1, t[1]))
                elif s[0] > t[0]:
                    if (t[0] + i + 1, t[1]) not in tlist:
                        oblist.append((t[0] + i + 1, t[1]))
            oblist_copy = oblist.copy()
            for ob in oblist_copy:
                if ob in slist:
                    oblist_copy.remove(ob)
            if oblist == oblist_copy:
                obstacle[f'Ob{obnum}'] = oblist
                obnum += 1

obnum -= 1

final = list(obstacle.values())
finale = []

# 리스트에서 중복되는 원소 제거
for oblist in final:
    if oblist not in finale:
        finale.append(oblist)
    elif oblist in finale:
        obnum -= 1

# 모든 선생님-학생 line을 그었을 때 교점이 있으면 그 좌표에 장애물을 설치하여 필요한 장애물의 갯수를 1개 줄일 수 있음
# 따라서 같은 좌표(교점)가 있을 때마다 장애물의 갯수에서 1을 차감
for i in range(len(finale)):
    a = finale[i]
    for j in range(i + 1, len(finale)):
        b = finale[j]
        for ob_a in a:
            for ob_b in b:
                if ob_a == ob_b:
                    obnum -= 1

# 리스트에 '[]'가 있으면 선생님과 학생 사이에 간격이 없다는 뜻이므로 감시를 피할 수 없음
if obnum <= 3:
    if [] in finale:
        print("NO")
    else:
        print("YES")
else:
    print("NO")