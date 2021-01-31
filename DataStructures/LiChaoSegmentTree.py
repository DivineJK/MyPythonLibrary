oper = lambda a, b: min(a, b)
jlf = lambda a, b, c, d, l: a*l + b < c*l + d
jmf = lambda a, b, c, d, m: a*m + b < c*m + d
jrf = lambda a, b, c, d, r: a*r + b < c*r + d
class li_chao_segment_tree:
    def __init__(self, n, op, judge_l, judge_m, judge_r, interval, INF_C, INF_S):
        self.n = n
        self.cnt = 0
        self.bin_top = 1
        self.op = op
        self.INF_C = INF_C
        self.INF_S = INF_S
        self.judge_l = judge_l
        self.judge_m = judge_m
        self.judge_r = judge_r
        while self.bin_top < n:
            self.cnt += 1
            self.bin_top <<= 1
        self.segtree = [(0, INF_S)]*(self.bin_top<<1)
        self.isvisited = [False]*(self.bin_top<<1)
        self.isvisited[0] = True
        self.interval = [(INF_C, INF_C)]*(self.bin_top<<1)
        l = len(interval)
        for i in range(l):
            if i < l-1:
                self.interval[i+self.bin_top] = (interval[i], interval[i+1])
            else:
                self.interval[i+self.bin_top] = (interval[i], INF_C)
        for i in range(self.bin_top, 0, -1):
            self.interval[i-1] = (self.interval[2*(i-1)][0], self.interval[2*i-1][1])
    def add_line(self, a, b):
        s, t = a, b
        pnt = 1
        while pnt < self.bin_top:
            if not self.isvisited[pnt]:
                self.isvisited[pnt] = True
                self.segtree[pnt] = (s, t)
                break
            (c, d) = self.segtree[pnt]
            (l, r) = self.interval[pnt]
            m = self.interval[pnt<<1][1]
            flg_l = self.judge_l(s, t, c, d, l)
            flg_m = self.judge_m(s, t, c, d, m)
            flg_r = self.judge_r(s, t, c, d, r)
            if flg_l and flg_r:
                self.segtree[pnt] = (s, t)
                break
            if not (flg_l or flg_r):
                break
            if flg_m:
                self.segtree[pnt] = (s, t)
                flg_l ^= 1
                flg_m ^= 1
                flg_r ^= 1
                s, t = c, d
            pnt <<= 1
            if flg_r:
                pnt += 1
        if not self.isvisited[pnt]:
            self.isvisited[pnt] = True
            self.segtree[pnt] = (s, t)
        elif pnt >= self.bin_top:
            (c, d) = self.segtree[pnt]
            (l, r) = self.interval[pnt]
            flg_l = self.judge_l(s, t, c, d, l)
            flg_r = self.judge_r(s, t, c, d, r)
            if flg_l:
                self.segtree[pnt] = (s, t)
    def get_segment(self, x):
        pnt = 1
        m = self.INF_S
        while pnt < self.bin_top:
            if not self.isvisited[pnt]:
                return m
            m = self.op(m, self.segtree[pnt][0]*x+self.segtree[pnt][1])
            pnt <<= 1
            if self.interval[pnt+1][0] <= x and x < self.interval[pnt+1][1]:
                pnt += 1
        m = self.op(m, self.segtree[pnt][0]*x+self.segtree[pnt][1])
        return m
