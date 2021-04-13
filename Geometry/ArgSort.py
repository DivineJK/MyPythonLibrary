class argument_sorting:
    def __init__(self, start_vec=(1, 0), zero_arg=(1, 0), left_include=0):
        self.start_vec = start_vec
        self.zero_arg = zero_arg
        self.left_include = left_include
        if start_vec == (0, 0):
            self.start_vec = (1, 0)
        if zero_arg == (0, 0):
            self.zero_arg = (1, 0)
    def inner_product(self, a, b):
        return a[0] * b[0] + a[1] * b[1]
    def outer_product(self, a, b):
        return a[0] * b[1] - a[1] * b[0]
    def chk_zone(self, a):
        if a == (0, 0):
            a = self.zero_arg
        ip = self.inner_product(self.start_vec, a)
        op = self.outer_product(self.start_vec, a)
        t = self.left_include
        if ip > 0 and op == 0:
            t += 0
        elif ip > 0 and op > 0:
            t += 1
        elif ip == 0 and op > 0:
            t += 2
        elif ip < 0 and op > 0:
            t += 3
        elif ip < 0 and op == 0:
            t += 4
        elif ip < 0 and op < 0:
            t += 5
        elif ip == 0 and op < 0:
            t += 6
        elif ip > 0 and op < 0:
            t += 7
        return t % 8
    def compare_argument(self, a, b):
        if self.chk_zone(a) != self.chk_zone(b):
            return self.chk_zone(a) < self.chk_zone(b)
        if self.outer_product(a, b):
            return self.outer_product(a, b) > 0
        return self.inner_product(a, a) <= self.inner_product(b, b)
    def bubble_arg_sort(self, pool, reverse=False):
        n = len(pool)
        res = [i for i in range(n)]
        for i in range(n-1, 0, -1):
            for j in range(i):
                if not (self.compare_argument(pool[res[j]], pool[res[j+1]]) ^ reverse):
                    res[j], res[j+1] = res[j+1], res[j]
        res_vec = [pool[res[i]] for i in range(n)]
        return res_vec
    def merge_arg_sort(self, pool, reverse=False):
        n = len(pool)
        if n == 1:
            return pool
        left = self.merge_arg_sort(pool[:n//2], reverse)
        right = self.merge_arg_sort(pool[n//2:], ~(reverse))
        pnt_l = 0
        pnt_r = n-n//2-1
        idx_r = [0 for _ in range(n)]
        for i in range(n):
            if pnt_l >= n // 2:
                idx_r[i] = pnt_r + n // 2
                pnt_r -= 1
            elif pnt_r < 0:
                idx_r[i] = pnt_l
                pnt_l += 1
            else:
                if self.compare_argument(left[pnt_l], right[pnt_r]):
                    if reverse:
                        idx_r[i] = pnt_r + n // 2
                        pnt_r -= 1
                    else:
                        idx_r[i] = pnt_l
                        pnt_l += 1
                else:
                    if reverse:
                        idx_r[i] = pnt_l
                        pnt_l += 1
                    else:
                        idx_r[i] = pnt_r + n // 2
                        pnt_r -= 1
        res = [(0, 0) for i in range(n)]
        for i in range(n):
            if idx_r[i] >= n // 2:
                res[i] = right[idx_r[i]-n//2]
            else:
                res[i] = left[idx_r[i]]
        return res
