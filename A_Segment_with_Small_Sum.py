[n, s] = list(map(int, input().split()))

a = list(map(int, input().split()))

i = j = tot = sz = ans = 0
while j < n:

    tot += a[j]
    sz += 1
    
    if tot <= s:
        ans = max(ans, sz)
    else:
        tot -= a[i]
        i += 1
        sz -= 1
    
    j += 1

print(ans)
    