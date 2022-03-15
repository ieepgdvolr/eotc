def solution(N, M, K, numbers):
    if M == K :
        return M * numbers[0]

    group = numbers[0] * K + numbers[1]
    a = M // (K+1)
    b = M % (K+1)

    return group * a + numbers[0] * b


if __name__ == '__main__':

    N, M, K = map(int, input().split())
    data = list(map(int, input().split()))

    numbers = list(set(data))
    numbers.sort(reverse=True)

    print(solution(N, M, K, numbers))
