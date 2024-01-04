[n, s] = list(map(int, input().split()))
a = list(map(int, input().split()))

i = j = tot = 0
ans = 1e9 + 7
ok = False
while j < n:
    tot += a[j]
    if tot >= s:
        while tot >= s and i <= j:
            ans = min(ans, j - i + 1)
            tot -= a[i]
            i += 1
            ok = True
    j += 1

if ok:
    print(ans)
else:
    print(-1)
