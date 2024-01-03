[n, m] = list(map(int, input().split()))

a = list(map(int, input().split()))
b = list(map(int, input().split()))

cnt = i = j = 0
while j < m:
    if a[i] < b[j]:
        cnt += 1
        if i == n - 1:
            print(cnt, end=' ')
            cnt -= 1
            j += 1
        else:
            i += 1
    else:
        print(cnt, end=' ')
        j += 1
