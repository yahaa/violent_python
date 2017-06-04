def solve(a):
    return abs(max(a) - min(a))


n, m = map(int, raw_input().split())
a = map(int, raw_input().split())
a.sort()
res = 2 << 31
for i in range(m - n + 1):
    t = a[i:i + n]
    res = min(solve(t), res)
print res
