# encoding=utf-8


def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)


def fibonacci(n):
    if n <= 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def next_permutation(arr, k, n):
    # 下一个全排列递归实现
    if k == n:
        print arr
    for i in range(k, n):
        arr[i], arr[k] = arr[k], arr[i]
        next_permutation(arr, k + 1, n)
        arr[i], arr[k] = arr[k], arr[i]


def next_permutation2(a):
    n = len(a)
    if n <= 1:
        return a

    for i in range(n, 1):
        if a[i - 1] < a[i]:
            pass

    pass


def zero_of_factorial_n(n):
    # 阶乘末尾０的个数
    res = 0
    while n > 0:
        res += n / 5
        res /= 5
    return res


def one_of_factorial_n(n):
    res = 0
    while n:
        n >>= 1
        res += n
    return res


def permutation_n(a, n):
    # 求一个序列的第n个字典排序序列,效率高但是空间复杂度高
    res = []
    l = len(a) - 1
    while n != 0:
        i = n / factorial(l)
        res.append(a[i])
        a.remove(a[i])
        n %= factorial(l)
        l -= 1
    a.sort()
    res.extend(a)
    return res


def permutation_n1(a):
    # 求一个序列的第n个字典排序序列,效率较低
    n = len(a)
    if not n:
        return
    i = n - 2
    while i >= 0 and a[i] >= a[i + 1]:
        i -= 1
    if i >= 0:
        j = n - 1
        while a[j] <= a[i]:
            j -= 1
        a[i], a[j] = a[j], a[i]
    left, right = i + 1, n - 1
    while left <= right:
        a[left], a[right] = a[right], a[left]
        left += 1
        right -= 1


def q_sort(a):
    # 快排
    def do_sort(a, left, right):
        if left >= right:
            return
        t = a[left]
        i, j = left, right
        while i != j:
            while a[j] >= t and i < j:
                j -= 1
            while a[i] <= t and i < j:
                i += 1
            if i < j:
                a[i], a[j] = a[j], a[i]
        a[left], a[i] = a[i], a[left]
        do_sort(a, left, i - 1)
        do_sort(a, i + 1, right)

    do_sort(a, 0, len(a) - 1)
    return a


def pao_sort(a):
    # 冒泡排序
    n = len(a)
    for i in range(n):
        for j in range(i, n):
            if a[i] > a[j]:
                a[i], a[j] = a[j], a[i]
    return a


def se_sort(a):
    # 选择排序
    n = len(a)
    for i in range(n):
        mi = i
        for j in range(i + 1, n):
            if a[j] < a[mi]:
                mi = j
        a[mi], a[i] = a[i], a[mi]
    return a


if __name__ == '__main__':
    print 1654 / 720
    print factorial(6)
    print fibonacci(5)
    a = ['a', 'b', 'c']

    next_permutation(a, 0, 3)

    b = [1, 2]
    print permutation_n1(b)
    print b
    n = 100
    print bin(n)
    print bin(-n)
    print bin(n & -n)
    print bin(factorial(5))
    print one_of_factorial_n(5)
    a = [2, 4, 1, 5, 3, 4, 4, 4, 4, 4, 78]
    print se_sort(a)
