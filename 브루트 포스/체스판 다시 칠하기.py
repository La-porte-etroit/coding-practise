# 백준 1018번 <체스판 다시 칠하기>

# 

N, M = map(int, input().split())
c1 = [['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']]
c2 = [['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B']]
board = []
for i in range(N):
    board.append(list(input()))
L = []

a = 0
while a+8 <= N:
    b = 0
    while b+8 <= M:
        num1 = 0
        num2 = 0
        x = 0
        for i in range(a, a+8):
            y = 0
            for j in range(b, b+8):
                if board[i][j] != c1[x][y]:
                    num1 += 1
                if board[i][j] != c2[x][y]:
                    num2 += 1
                y += 1
            x += 1
        L.append(num1)
        L.append(num2)
        b += 1
    a += 1
    
print(min(L))