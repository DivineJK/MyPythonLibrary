# EDPC-V
# ------ preparation of tree ------
N, M = map(int, input().split())
mod = M
graph = [[] for _ in range(N)]
for i in range(N-1):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)
p = [0] # root -> folia
child = [[] for _ in range(N)]
child_cnt = [0]*N
par = [-1]*N
depth = [-1]*N
par[0] = 0
depth[0] = 0
for i in range(N):
    c = p[i]
    for j in graph[c]:
        if par[j] < 0:
            par[j] = c
            child[c].append(j)
            depth[j] = depth[c] + 1
            child_cnt[c] += 1
            p.append(j)
size = [1]*N
for i in range(N-1, 0, -1):
    u = p[i]
    c = par[u]
    size[c] += size[u]
V = [-1]*N
for i in range(N):
    for j in range(child_cnt[i]):
        V[child[i][j]] = j

# ------ dp for rooted tree ------
dp1 = [1]*N
for i in range(N, 0, -1):
    u = p[i-1]
    for j in child[u]:
        dp1[u] = dp1[u] * (dp1[j] + 1) % mod
L = [[] for i in range(N)] # cumulative product for leftside
R = [[] for i in range(N)] # cumulative product for rightside
for i in range(N):
    if child_cnt[i]:
        L[i] = [dp1[child[i][0]]+1]*child_cnt[i]
        R[i] = [dp1[child[i][-1]]+1]*child_cnt[i]
for i in range(N):
    for j in range(child_cnt[i]-1):
        L[i][j+1] = L[i][j] * (dp1[child[i][j+1]] + 1) % mod
        R[i][child_cnt[i]-2-j] = R[i][child_cnt[i]-1-j] * (dp1[child[i][child_cnt[i]-j-2]] + 1) % mod
f = [[1]*child_cnt[i] for i in range(N)]
for i in range(N):
    for j in range(1, child_cnt[i]-1):
        f[i][j] = L[i][j-1] * R[i][j+1] % mod
    if child_cnt[i] >= 2:
        f[i][0] = R[i][1]
        f[i][-1] = L[i][-2]
# ------ Rerooting ------
dp2 = [1]*N
for i in range(1, N):
    t = p[i]
    u = par[t]
    dp2[t] = (1 + dp2[u] * f[u][V[t]])% mod
for i in range(N):
    print(dp1[i] * dp2[i] % mod)
