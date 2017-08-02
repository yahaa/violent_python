def bits(n):
    count = 0
    while n > 0:
        n -= n & -n
        count += 1
    return count


if __name__ == '__main__':
    print bits(2)
