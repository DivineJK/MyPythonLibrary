def stola(s):
    if len(s) == 0:
        return [0]
    v = []
    m = 0
    for i, k in enumerate(s):
        v.append(ord(k))
        if i == 0:
            m = v[0]
        m = min(v[i], m)
    return v[:] + [m-1]
def bucket_sort(v, ls, seed):
    n = len(v)
    m = len(seed)
    f = {}
    for i in v:
        f[i] = 0
    for i in range(n):
        f[v[i]] += 1
    idx = sorted([i for i in f])
    y = len(idx)
    inv_idx = {idx[i]: i for i in range(y)}
    l_idx = [0]*y
    r_idx = [0]*y
    r_idx[0] = f[idx[0]] - 1
    for i in range(1, y):
        l_idx[i] = l_idx[i-1] + f[idx[i-1]]
        r_idx[i] = r_idx[i-1] + f[idx[i]]
    res = [-1]*n
    for i in range(m, 0, -1):
        ch = v[seed[i-1]]
        ii = inv_idx[ch]
        res[r_idx[ii]] = seed[i-1]
        r_idx[ii] -= 1
    for i in range(n):
        if res[i] > 0:
            if not ls[res[i]-1]:
                ch = v[res[i]-1]
                ii = inv_idx[ch]
                res[l_idx[ii]] = res[i] - 1
                l_idx[ii] += 1
    r_idx[0] = f[idx[0]] - 1
    for i in range(1, y):
        r_idx[i] = r_idx[i-1] + f[idx[i]]
    for i in range(n, 0, -1):
        if res[i-1] > 0:
            if ls[res[i-1]-1]:
                ch = v[res[i-1]-1]
                ii = inv_idx[ch]
                res[r_idx[ii]] = res[i-1] - 1
                r_idx[ii] -= 1
    return res
def suffix_array(s):
    n = len(s)
    v = [0]*n
    for i, k in enumerate(s):
        v[i] = k
    ls = [True]*n
    for i in range(n-1, 0, -1):
        if v[i-1] > v[i]:
            ls[i-1] = False
        elif v[i-1] == v[i]:
            ls[i-1] = ls[i]
    lms = [False]*n
    lms_idx = []
    inv_lms_idx = {}
    lms_cnt = 0
    lms[0] = ls[0]
    if ls[0]:
        inv_lms_idx[0] = lms_cnt
        lms[0] = True
        lms_idx.append(0)
        lms_cnt += 1
    for i in range(n-1):
        if ls[i+1] and not ls[i]:
            lms[i+1] = True
            lms_idx.append(i+1)
            inv_lms_idx[i+1] = lms_cnt
            lms_cnt += 1
    sa = bucket_sort(v, ls, lms_idx)
    prev = sa[0]
    sa_lms = [0]*lms_cnt
    pnt = 0
    for i in range(n):
        if lms[sa[i]]:
            sa_lms[pnt] = sa[i]
            pnt += 1
    #print(sa_lms)
    new_lms = [-1]*lms_cnt
    new_lms[inv_lms_idx[sa_lms[0]]] = 0
    num = 0
    for i in range(1, lms_cnt):
        flg = False
        l_pos, r_pos = prev, sa_lms[i]
        for d in range(n):
            if v[l_pos+d] != v[r_pos+d] or lms[l_pos+d] != lms[r_pos+d]:
                flg = True
                break
            elif d > 0 and (lms[l_pos+d] or lms[r_pos+d]):
                break
        if flg:
            num += 1
        new_lms[inv_lms_idx[sa_lms[i]]] = num
        #print(prev, new_lms, sa_lms[i], flush=True)
        prev = sa_lms[i]
    seed = [0]*lms_cnt
    nums = [0]*lms_cnt
    if num + 1 < lms_cnt:
        nums = suffix_array(new_lms)
        #print(True, *new_lms, lms_cnt)
    else:
        #print(False, *new_lms, lms_cnt)
        #for i in range(lms_cnt):
        #    new_lms[i] -= 1
        #print(*new_lms, flush=True)
        for i in range(lms_cnt):
            nums[new_lms[i]] = i
    #print(inv_lms_idx, lms_cnt, new_lms, flush=True)
    for i in range(lms_cnt):
        seed[i] = lms_idx[nums[i]]
    #print(*new_lms, flush=True)
    sa = bucket_sort(v, ls, seed)
    return sa
