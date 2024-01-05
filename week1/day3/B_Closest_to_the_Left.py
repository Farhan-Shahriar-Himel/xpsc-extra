from bisect import bisect

[n, q] = list(map(int, input().split()))
a = list(map(int, input().split()))
queries = list(map(int, input().split()))

for x in queries:
    print(bisect(a, x))
