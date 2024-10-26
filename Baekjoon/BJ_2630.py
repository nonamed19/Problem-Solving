from pprint import pprint

def papercuts(row, column, N):
    global white, blue

    color = papers[row][column]
    for i in range(row, row + N):
        for j in range(column, column + N):
            if color != papers[i][j]:
                papercuts(row, column, N//2)
                papercuts(row+N//2, column, N//2)
                papercuts(row, column+N//2, N//2)
                papercuts(row+N//2, column+N//2, N//2)
                return
    if color == 0:
        white += 1
    else:  # elif color == 1:
        blue += 1


N = int(input())  # N = 2, 4, 8, 16, 32, 64, 128
papers = [list(map(int, input().split())) for _ in range(N)]

white, blue = 0, 0
papercuts(row = 0, column = 0, N = N)

print(white)
print(blue)