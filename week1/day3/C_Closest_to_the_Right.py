from bisect import bisect_left

[n, q] = list(map(int, input().split()))
a = list(map(int, input().split()))
queries = list(map(int, input().split()))

for x in queries:
    print(bisect_left(a, x) + 1)
