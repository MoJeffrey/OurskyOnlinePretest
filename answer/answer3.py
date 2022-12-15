import sys
import time


def recur(n, cur):
    if cur is None:
        cur = 0

    if n < 2:
        raise Exception('Invalid input')

    elif n == 2:
        return 1 / n + cur

    return recur(n - 1, cur + 1 / (n * (n - 1)))


def rewriteRecur(n, cur):
    if cur is None:
        cur = 0

    if n < 2:
        raise Exception('Invalid input')

    elif n == 2:
        return 1 / n + cur
    else:
        for newN in range(n, 2, -1):
            cur = cur + 1 / (newN * (newN - 1))
        return 1 / 2 + cur


if __name__ == '__main__':
    sys.setrecursionlimit(100000)

    startTime = time.time()
    result = recur(100000, 6465)
    endTime = time.time()
    print(f"舊算法结果: {result}, 運行時間： {endTime - startTime}ms")

    startTime = time.time()
    result = rewriteRecur(100000, 6465)
    endTime = time.time()
    print(f"新算法结果: {result}, 運行時間： {endTime - startTime}ms")
