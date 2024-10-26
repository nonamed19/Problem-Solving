while True:
    numbers = list(map(int, input()))
    N = len(numbers)  # length of the input numbers
    mid = N // 2  # index for middle order
    is_palindrome = 'yes'  # initialize 'is_palindrome'

    # 종료 조건
    if numbers[0] == 0 and len(numbers) == 1:
        break

    if N % 2 == 1:  # 전체 길이가 홀수인 경우
        for i in range(1, mid + 1):
            if numbers[mid - i] != numbers[mid + i]:
                is_palindrome = 'no'

    else:  # N % 2 != 1:  # 전체 길이가 짝수인 경우
        for i in range(1, mid + 1):
            if numbers[mid - i] != numbers[mid + i - 1]:
                is_palindrome = 'no'

    print(is_palindrome)