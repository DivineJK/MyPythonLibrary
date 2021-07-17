def getInOutTime(parent):
    # note: make sure that parent[start] == -1
    n = len(parent)
    start = 0
    while parent[start] != -1:
        start += 1
    child_num = [0]*n
    counts = [0]*n
    child_pnt = [0]*n
    children = [[] for _ in range(n)]
    for i in range(n):
        if i == start:
            continue
        children[parent[i]].append(i)
        if child_num[parent[i]] == 0:
            child_pnt[i] = -1
        else:
            child_pnt[i] = children[parent[i]][child_num[parent[i]]-1]
        child_num[parent[i]] += 1
    now_v = start
    order = [-1]*n
    order[now_v] = 0
    d = 1
    while True:
        if counts[now_v] < child_num[now_v]:
            tmp = counts[now_v]
            counts[now_v] += 1
            now_v = children[now_v][tmp]
            if order[now_v] == -1:
                order[now_v] = d
                d += 1
        else:
            if now_v == start:
                break
            now_v = parent[now_v]
    visit_map = [0]*n
    for i in range(n):
        visit_map[order[i]] = i
    p = []
    pnt = 0
    cnt = 0
    flg = [0]*n
    child_total = [0]*n
    for i in range(n):
        if child_num[i] == 0:
            p.append(i)
            cnt += 1
    while pnt < cnt:
        nn = cnt
        for i in range(pnt, cnt):
            c = p[i]
            if c != start:
                child_total[parent[c]] += child_total[c] + 1
                flg[parent[c]] += 1
                if flg[parent[c]] == child_num[parent[c]]:
                    p.append(parent[c])
                    cnt += 1
        pnt = nn
    intime = [0]*n
    outtime = [0]*n
    outtime[start] = 2 * n - 1
    for i in range(1, n):
        c = visit_map[i]
        if child_pnt[c] == -1:
            intime[c] = intime[parent[c]] + 1
        else:
            intime[c] = outtime[child_pnt[c]] + 1
        outtime[c] = intime[c] + 2 * child_total[c] + 1
    return intime, outtime
