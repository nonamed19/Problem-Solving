C = int(input())

average = 0
for _ in range(C):
    N, *scores = list(map(int, input().split()))
    average = sum(scores) / N  # 평균 점수
    above_average = sum(score > average for score in scores)  # 평균을 넘는 학생들의 수

    print(f'{above_average / N * 100:.3f}%')
