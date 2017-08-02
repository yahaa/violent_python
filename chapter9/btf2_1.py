# encoding=utf-8


def bits(n):
    # 求一个数二进制中１的个数
    count = 0
    while n > 0:
        n -= n & -n
        count += 1
    return count


def factorial_0(n):
    # 求阶层中末尾０的个数
    def way1(n):
        res = 0
        for (i in range(1, n + 1)):
            j = i
            while j % 5 == 0:
                res += 1
                j /= 5
        return res


if __name__ == '__main__':
    print bits(2)
