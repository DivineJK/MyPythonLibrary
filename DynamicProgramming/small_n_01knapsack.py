class small_n_01knapsack:
    def __init__(self, weight_limit, value_identity=0):
        self.item_cnt = 0
        self.wl = weight_limit
        self.d_first = [(0, value_identity)]
        self.d_second = [(0, value_identity)]
    def add_item(self, w, v):
        cnt = self.item_cnt >> 1
        if self.item_cnt & 1:
            for i in range(1<<cnt):
                tmp_w, tmp_v = self.d_second[i][0] + w, self.d_second[i][1] + v
                if tmp_w <= self.wl:
                    self.d_second.append((tmp_w, tmp_v))
                else:
                    self.d_second.append((self.wl+1, 0))
        else:
            for i in range(1<<cnt):
                tmp_w, tmp_v = self.d_first[i][0] + w, self.d_first[i][1] + v
                if tmp_w <= self.wl:
                    self.d_first.append((tmp_w, tmp_v))
                else:
                    self.d_first.append((self.wl+1, 0))
        self.item_cnt += 1
    def solver(self):
        self.d_second.sort()
        l_second = []
        ls_cnt = 0
        for i in self.d_second:
            if i[0] <= self.wl:
                ls_cnt += 1
                l_second.append(i[1])
        for i in range(1, ls_cnt-1):
            if l_second[i] < l_second[i-1]:
                l_second[i] = l_second[i-1]
        res = 0
        for i in self.d_first:
            w, v = i[0], i[1]
            if w > self.wl:
                continue
            l, r = 0, ls_cnt
            m = (l + r) // 2
            while r - l > 1:
                if self.d_second[m][0] + w <= self.wl:
                    l = m
                else:
                    r = m
                m = (l + r) // 2
            if res < v + l_second[m]:
                res = v + l_second[m]
        return res
