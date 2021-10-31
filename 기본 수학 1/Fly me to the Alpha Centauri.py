n = int(input())
case_list = []

for i in range(n):
    test = []
    a, b = map(int, input().split())
    test.extend([a, b])
    case_list.append(test)

for case in case_list:
    d = case[1] - case[0]
    k = 1
    while True:
        if k*(k + 1) >= d:
            if d > k**2:
                print(2*k)
                break
            else:
                print(2*k - 1)
                break
        else:
            k += 1

    # sub = 1
    # num = 1
    # k = 0
    
    # while sub <= obj:
    #     k += 1
    #     if sub != obj:
    #         sub += 1
    #         if k == num*2:
    #             k = 0
    #             num += 1
    #     else:
    #         if k > num:
    #             print(num*2)
    #             break
    #         else:
    #             print(num*2 - 1)
    #             break


# 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 (거리)
# 1 2 3 3 4 4 5 5 5 6  6  6  7  7  7  7  8  8  8  8  9  9  9  9  9  (장치 작동 횟수)
# 1 1 2 2 2 2 3 3 3 3  3  3  4  4  4  4  4  4  4  4  5  5  5  5  5  (반복 횟수)