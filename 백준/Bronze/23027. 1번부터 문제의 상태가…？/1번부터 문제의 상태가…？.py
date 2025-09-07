import sys
input = sys.stdin.readline


S = input().strip()

# 1. 편지의 내용 S에 'A'가 있다면 S에 있는 'B', 'C', 'D', 'F'를 모두 'A'로 변경한다.
if 'A' in S:
    S = S.replace('B', 'A')
    S = S.replace('C', 'A')
    S = S.replace('D', 'A')
    S = S.replace('F', 'A')

# 2. 'A'가 없고 'B'가 있다면 S에 있는 'C', 'D', 'F'를 모두 'B'로 변경한다.
elif 'B' in S:
    S = S.replace('C', 'B')
    S = S.replace('D', 'B')
    S = S.replace('F', 'B')

# 3. 'A'와 'B'가 없고 'C'가 있다면 S에 있는 'D', 'F'를 모두 'C'로 변경한다.
elif 'C' in S:
    S = S.replace('D', 'C')
    S = S.replace('F', 'C')

# 4. 'A', 'B'와 'C'가 모두 없다면 S에 있는 모든 문자를 'A'로 변경한다.
else:
    S = 'A'*len(S)

print(S)
