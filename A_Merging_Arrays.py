[n, m] = list(map(int, input().split()))

a = list(map(int, input().split())) + [1e9 + 7]
b = list(map(int, input().split())) + [1e9 + 7]

a.sort()
b.sort()

res = []
lp = rp = 0
sz = n + m

while len(res) != sz:
    if a[lp] < b[rp]:
        res.append(a[lp])
        lp += 1
    else:
        res.append(b[rp])
        rp += 1

print(*res)
