import IntLib as IL

class safety_sqrt:
    def parse_sqrt(self, n: int):
        sign = 1
        n1 = n
        if n == 0:
            return {}
        if n < 0:
            sign = -1
            n1 = -n
        nd = IL.factorization(n1)
        val = 1
        res = 1
        for i in nd:
            val *= IL.doubling(i, nd[i]//2)
            res *= IL.doubling(i, nd[i]%2)
        return {sign*res: [val, 1]}
    def trim_sqrt(self, d):
        new_d = {}
        for i in d:
            if i == 0:
                continue
            s = self.parse_sqrt(i)
            tmp = 0
            for k in s:
                tmp = k
            r = IL.frac_prod(s[tmp], d[i])
            if i in new_d:
                new_d[tmp] = IL.frac_sum(r, new_d[i])
            else:
                new_d[tmp] = r
        return new_d
    def sqrt_sum(self, s1: dict, s2: dict, weight=1):
        n1 = self.trim_sqrt(s1)
        n2 = self.trim_sqrt(s2)
        prev_res = {i: n1[i] for i in n1}
        for i in n2:
            if i in prev_res:
                prev_res[i] = IL.frac_sum(prev_res[i], n2[i], weight)
            else:
                prev_res[i] = IL.frac_sum([0, 1], n2[i], weight)
        res = {}
        for i in prev_res:
            if prev_res[i][0]:
                res[i] = prev_res[i]
        return res
    def sqrt_prod(self, s1: dict, s2: dict):
        n1 = self.trim_sqrt(s1)
        n2 = self.trim_sqrt(s2)
        prev_res = {}
        for i in n1:
            for j in n2:
                out_sign = 1
                if i < 0 and j < 0:
                    out_sign = -1
                s = self.parse_sqrt(i*j)
                tmp = 0
                for k in s:
                    tmp = k
                v = IL.frac_prod(n1[i], n2[j])
                v = IL.frac_prod(v, s[tmp])
                v = IL.frac_prod(v, [out_sign, 1])
                if tmp in prev_res:
                    prev_res[tmp] = IL.frac_sum(v, prev_res[tmp])
                else:
                    prev_res[tmp] = v
        res = {}
        for i in prev_res:
            if prev_res[i][0]:
                res[i] = prev_res[i]
        res = self.trim_sqrt(res)
        return res
    def sqrt_inv(self, s: dict):
        s = self.trim_sqrt(s)
        if s == {}:
            raise RuntimeError("Division by zero.") from None
        d1 = {1: [1, 1]}
        d2 = {i: s[i] for i in s}
        while 1 not in d2 or len(d2) > 1:
            left, right = {}, {}
            pivot = 0
            imag = False
            for k in d2:
                if k < 0:
                    imag = True
                    break
            if imag:
                pivot = -1
            else:
                for k in d2:
                    if k != 1:
                        pivot = k
                        break
            for i in d2:
                if pivot > 0:
                    if i % pivot:
                        left[i] = d2[i]
                    else:
                        right[i//pivot] = d2[i]
                else:
                    if i < 0:
                        right[-i] = d2[i]
                    else:
                        left[i] = d2[i]
            right = self.sqrt_prod(right, {pivot: [1, 1]})
            d1 = self.sqrt_prod(d1, self.sqrt_sum(left, right, -1))
            left = self.sqrt_prod(left, left)
            right = self.sqrt_prod(right, right)
            d2 = self.sqrt_sum(left, right, -1)
        for i in d1:
            d1[i] = IL.frac_prod(d1[i], d2[1], True)
        return d1
    def sqrt_frac(self, s1: dict, s2: dict):
        s1 = self.trim_sqrt(s1)
        return self.sqrt_prod(s1, sqrt_inv(s2))
