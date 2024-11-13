import sys

def moving(king, stone, move):
    temp = king[:]  # temporary position for king

    if move == 'R':  # R : 한 칸 오른쪽으로
        temp[1] += 1
        if temp == stone and 1 <= stone[1] + 1 <= 8:  # stone의 boundary condition
            stone[1] += 1
            king[1] += 1
        elif temp == stone:  # stone으로 인해 king이 움직일 수 없는 경우
            pass
        elif 1 <= king[1] + 1 <= 8:  # king의 boundary condition
            king[1] += 1

    elif move == 'L':  # L : 한 칸 왼쪽으로
        temp[1] -= 1
        if temp == stone and 1 <= stone[1] - 1 <= 8:  # stone의 boundary condition
            stone[1] -= 1
            king[1] -= 1
        elif temp == stone:  # stone으로 인해 king이 움직일 수 없는 경우
            pass
        elif 1 <= king[1] - 1 <= 8:  # king의 boundary condition
            king[1] -= 1

    elif move == 'B':  # B : 한 칸 아래로
        temp[0] -= 1
        if temp == stone and 1 <= stone[0] - 1 <= 8:  # stone의 boundary condition
            stone[0] -= 1
            king[0] -= 1
        elif temp == stone:  # stone으로 인해 king이 움직일 수 없는 경우
            pass
        elif 1 <= king[0] - 1 <= 8:  # king의 boundary condition
            king[0] -= 1

    elif move == 'T':  # T : 한 칸 위로
        temp[0] += 1
        if temp == stone and 1 <= stone[0] + 1 <= 8:  # stone의 boundary condition
            stone[0] += 1
            king[0] += 1
        elif temp == stone:  # stone으로 인해 king이 움직일 수 없는 경우
            pass
        elif 1 <= king[0] + 1 <= 8:  # king의 boundary condition
            king[0] += 1

    elif move == 'RT':  # RT : 오른쪽 위 대각선으로
        temp[0] += 1
        temp[1] += 1
        if temp == stone and 1 <= stone[0] + 1 <= 8 and 1 <= stone[1] + 1 <= 8:  # stone의 boundary condition
            stone[0] += 1
            stone[1] += 1
            king[0] += 1
            king[1] += 1
        elif temp == stone:  # stone으로 인해 king이 움직일 수 없는 경우
            pass
        elif 1 <= king[0] + 1 <= 8 and 1 <= king[1] + 1 <= 8:  # king의 boundary condition
            king[0] += 1
            king[1] += 1

    elif move == 'LT':  # LT : 왼쪽 위 대각선으로
        temp[0] += 1
        temp[1] -= 1
        if temp == stone and 1 <= stone[0] + 1 <= 8 and 1 <= stone[1] - 1 <= 8:  # stone의 boundary condition
            stone[0] += 1
            stone[1] -= 1
            king[0] += 1
            king[1] -= 1
        elif temp == stone:  # stone으로 인해 king이 움직일 수 없는 경우
            pass
        elif 1 <= king[0] + 1 <= 8 and 1 <= king[1] - 1 <= 8:  # king의 boundary condition
            king[0] += 1
            king[1] -= 1

    elif move == 'RB':  # RB : 오른쪽 아래 대각선으로
        temp[0] -= 1
        temp[1] += 1
        if temp == stone and 1 <= stone[0] - 1 <= 8 and 1 <= stone[1] + 1 <= 8:  # stone의 boundary condition
            stone[0] -= 1
            stone[1] += 1
            king[0] -= 1
            king[1] += 1
        elif temp == stone:  # stone으로 인해 king이 움직일 수 없는 경우
            pass
        elif 1 <= king[0] - 1 <= 8 and 1 <= king[1] + 1 <= 8:  # king의 boundary condition
            king[0] -= 1
            king[1] += 1

    elif move == 'LB':  # LB : 왼쪽 아래 대각선으로

        temp[0] -= 1
        temp[1] -= 1
        if temp == stone and 1 <= stone[0] - 1 <= 8 and 1 <= stone[1] - 1 <= 8:  # stone의 boundary condition
            stone[0] -= 1
            stone[1] -= 1
            king[0] -= 1
            king[1] -= 1
        elif temp == stone:  # stone으로 인해 king이 움직일 수 없는 경우
            pass
        elif 1 <= king[0] - 1 <= 8 and 1 <= king[1] - 1 <= 8:  # king의 boundary condition
            king[0] -= 1
            king[1] -= 1

    return king, stone


dic_position = {'A': 1, 'B': 2, 'C': 3, 'D': 4,
                'E': 5, 'F': 6, 'G': 7, 'H': 8}
dic_position_rev = {v:k for k, v in dic_position.items()}
king, stone, N = map(str, sys.stdin.readline().split())

king = [int(king[1]), dic_position[king[0]]]  # position initialization, format == [1, 1]
stone = [int(stone[1]), dic_position[stone[0]]]  # position initialization, format == [1, 2]
N = int(N)

moves = []
for _ in range(N):
    moves.append(sys.stdin.readline().strip())

for move in moves:
    king, stone = moving(king, stone, move)

king = dic_position_rev[king[1]] + str(king[0])
stone = dic_position_rev[stone[1]] + str(stone[0])

print(king)
print(stone)