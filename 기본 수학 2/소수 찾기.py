a = int(input())
nums = map(int, input().split())

ans = 0
for num in nums:
    if num == 1:
        continue
    elif num == 2:
        ans += 1
    else:
        d = 2
        while d <= num:
            if d == num:
                ans += 1
                break
            else:
                if num%d == 0:
                    break
                else:
                    d += 1

print(ans)