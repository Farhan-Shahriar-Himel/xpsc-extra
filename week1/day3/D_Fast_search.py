from bisect import bisect, bisect_left

n = int(input())
a = list(map(int, input().split()))
a.sort()

for _ in range(int(input())):
    [left, right] = list(map(int, input().split()))
    lp = bisect_left(a, left)
    rp = bisect(a, right)
    print(rp - lp, end=' ')