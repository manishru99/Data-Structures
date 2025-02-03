t = int(input())
v = []
for _ in range(t):
    n, m = map(int, input().split())
    v.append([m, n])
    
    for pair in v:
        ans = max(pair[0], pair[1]) + 1
    print(ans)