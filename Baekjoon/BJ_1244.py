def switch(gender, loc):
    loc_now = loc
    if gender == 1:
        while loc_now <= N:
            lst[loc_now] = 1 - lst[loc_now]
            loc_now += loc
    elif gender == 2:
        lst[loc_now] = 1 - lst[loc_now]
        step = 1
        left = loc_now - step
        right = loc_now + step
        while True:
            if 0 <= left and right <= N and lst[left] == lst[right]:
                lst[left] = 1 - lst[left]
                lst[right] = 1 - lst[right]
                left -= step
                right += step
            else:
                return

N = int(input())
lst = list(map(int, input().split()))
lst.insert(0, -1)   # index를 맞추기 위해 임시로 추가

num_stu = int(input())
lst_stu = [[0, 0]]*num_stu

for i in range(num_stu):
    n1, n2 = list(map(int, input().split()))
    switch(n1, n2)

lst.remove(-1)             # 임시로 추가한 -1 삭제
for i in lst: print(i)