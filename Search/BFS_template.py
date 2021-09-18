vec4 = [(0, 1), (0, -1), (1, 0), (-1, 0)]
vec8 = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

start = []
pnt = 0
cnt = len(start)
tim = 0
while pnt < cnt:
    tmp = pnt
    tim += 1
    for pnter in range(pnt, cnt):
        x = start[pnter]
        for j in next_vec[x]:
            if f:
                # g
                # st.append()
                cnt += 1
    cnt = pnter

"""
# AGC019F - Yes or No

N, M = map(int, input().split())
mod = 998244353
def gcd(x, y):
    while y:
        x, y = y, x % y
    return x
dp = [[0]*(M+1) for i in range(N+1)]
for i in range(N+1):
    dp[i][0] = i
for i in range(M+1):
    dp[0][i] = i
for i in range(N):
    for j in range(M):
        dp[i+1][j+1] = ((i+1)*dp[i][j+1]+(j+1)*dp[i+1][j]+max(i+1, j+1))*pow(i+j+2, mod-2, mod)%mod
print(dp[N][M])
"""
