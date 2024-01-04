[n, s] = list(map(int, input().split()))
a = list(map(int, input().split()))
 
i = j = tot = 0
ans = 0
while j < n:
    tot += a[j]
    while tot >= s and i <= j:
        ans += (n - j)
        tot -= a[i]
        i += 1
    j += 1
 
print(ans)