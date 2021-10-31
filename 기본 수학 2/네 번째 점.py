arr1 = []
arr2 = []

for _ in range(3):
    a, b = map(int, input().split())
    arr1.append(a)
    arr2.append(b)

if arr1[0] == arr1[1]:
    print(arr1[2], end = ' ')
elif arr1[0] == arr1[2]:
    print(arr1[1], end = ' ')
elif arr1[1] == arr1[2]:
    print(arr1[0], end = ' ')

if arr2[0] == arr2[1]:
    print(arr2[2])
elif arr2[0] == arr2[2]:
    print(arr2[1])
elif arr2[1] == arr2[2]:
    print(arr2[0])