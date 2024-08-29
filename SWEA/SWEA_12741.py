for tc in range(int(input())):
    A, B, C, D = map(int, input().split())
    if B < C:
        print(f'#{tc+1} {0}')
    elif A<C and D<B:
        print(f'#{tc+1} {D-C}')
    elif C<B:
        print(f'#{tc+1} {B-C}')