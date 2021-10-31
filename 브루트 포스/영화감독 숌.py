# 백준 1436번 <영화감독 숌>
# 
# 알고리즘:
# 첫 번째 종말의 숫자인 666부터 시작해서 while문 안에서 수에 1을 더해 가며 그 수가 종말의 숫자인지 판단한다.
# 종말의 숫자라면 count라는 변수에 1을 더하고, count와 N의 값이 같다면 반복문이 종료된다.
# 종말의 숫자가 아니라면 반복문을 계속 실행한다.


N = int(input())
count = 0  # 몇 번째 종말의 숫자인지를 나타내는 변수
n = 666

while True:
    a = True
    m = str(n)  # n을 문자열로 바꾸어서 각 자리 숫자를 하나씩 가져올 수 있게 하였음.
    for i in range(len(m)):
        if m[i] == '6':  # 처음으로 6이 등장했을 때
            try:
                if m[i+1] == m[i+2] == '6':  # 다음, 다다음 숫자도 6이라면? -> 종말의 숫자!
                    count += 1  # 이 수는 count번째 종말의 숫자임.
                    if count == N:
                        print(n)
                        a = False
                    break
            except:
                continue
    if a == False:
        break
    n += 1