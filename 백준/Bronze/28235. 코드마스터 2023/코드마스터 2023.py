import sys
input = sys.stdin.readline

cheering = {
    'SONGDO': 'HIGHSCHOOL',
    'CODE': 'MASTER',
    '2023': '0611',
    'ALGORITHM': 'CONTEST'
}

word = input().strip()

print(cheering[word])
