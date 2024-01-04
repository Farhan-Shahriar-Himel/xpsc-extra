[n, s] = list(map(int, input().split()))
a = list(map(int, input().split()))

i = j = tot = ans = 0
canAdd = True
while j < n:
    if canAdd:
        tot += a[j]
    if tot <= s:
        ans += j - i + 1
        j += 1
        canAdd = True
    else:
        tot -= a[i]
        i += 1
        canAdd = False

print(ans)
