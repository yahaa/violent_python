n = int(raw_input())
su = [0, 0, 0]
for i in range(n):
    j = 0
    for a in map(int, raw_input().split()):
        su[j] += a
        j += 1
f = 0
for i in su:
    if i == 0:
        f += 1

if f == 3:
    print 'YES'
else:
    print 'NO'
