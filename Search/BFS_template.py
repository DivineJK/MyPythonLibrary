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
