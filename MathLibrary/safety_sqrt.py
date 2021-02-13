class safety_sqrt:
    def factorization(self, n):
        a = n
        D = []
        p = 2
        cnt = 0
        while a % p == 0:
            a //= p
            cnt += 1
        if cnt:
            D.append((p, cnt))
        p += 1
        while a != 1:
            cnt = 0
            while a % p == 0:
                cnt += 1
                a //= p
            if cnt:
                D.append((p, cnt))
            p += 2
            if p * p > n and a != 1:
                D.append((a, 1))
                break
        return D
    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a
    def make_fact(self, n):
        if n > self.fact_cnt:
            self.fact = self.fact[:] + [0]*(n-self.fact_cnt)
            for i in range(self.fact_cnt, n):
                self.fact[i+1] = self.fact[i] * (i + 1)
            self.fact_cnt = n
    def frac_sum(self, f1, f2, weight=1):
        f = [f1[0]*f2[1]+weight*f2[0]*f1[1], f1[1]*f2[1]]
        g = gcd(f[0], f[1])
        f[0] //= g
        f[1] //= g
        if f[1] < 0:
            f[0] = -f[0]
            f[1] = -f[1]
        return f
    def frac_prod(self, f1, f2, inverse=False):
        if inverse:
            f = [f1[0]*f2[1], f1[1]*f2[0]]
        else:
            f = [f1[0]*f2[0], f1[1]*f2[1]]
        g = self.gcd(f[0], f[1])
        f[0] //= g
        f[1] //= g
        if f[1] < 0:
            f[0] = -f[0]
            f[1] = -f[1]
        return f
    def parse_sqrt(self, n):
        sign = 1
        n1 = n
        if n == 0:
            return {}
        if n < 0:
            sign = -1
            n1 = -n
        nd = self.factorization(n1)
        val = 1
        res = 1
        for i in nd:
            val *= pow(i[0], i[1]//2)
            res *= pow(i[0], i[1]%2)
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
            r = self.frac_prod(s[tmp], d[i])
            if i in new_d:
                new_d[tmp] = self.frac_sum(r, new_d[i])
            else:
                new_d[tmp] = r
        return new_d
    def sqrt_sum(self, s1, s2, weight=1):
        n1 = self.trim_sqrt(s1)
        n2 = self.trim_sqrt(s2)
        prev_res = {i: n1[i] for i in n1}
        for i in n2:
            if i in prev_res:
                prev_res[i] = self.frac_sum(prev_res[i], n2[i], weight)
            else:
                prev_res[i] = self.frac_sum([0, 1], n2[i], weight)
        res = {}
        for i in prev_res:
            if prev_res[i][0]:
                res[i] = prev_res[i]
        return res
    def sqrt_prod(self, s1, s2):
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
                v = self.frac_prod(n1[i], n2[j])
                v = self.frac_prod(v, s[tmp])
                v = self.frac_prod(v, [out_sign, 1])
                if tmp in prev_res:
                    prev_res[tmp] = self.frac_sum(v, prev_res[tmp])
                else:
                    prev_res[tmp] = v
        res = {}
        for i in prev_res:
            if prev_res[i][0]:
                res[i] = prev_res[i]
        res = self.trim_sqrt(res)
        return res
    def sqrt_inv(self, s):
        s = self.trim_sqrt(s)
        if s == {}:
            return {1: [1, 0]}
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
            d1[i] = self.frac_prod(d1[i], d2[1], True)
        return d1
    def sqrt_pow(self, s, n):
        res = {1: [1, 1]}
        bas = {i: s[i] for i in s}
        if n < 0:
            bas = self.sqrt_inv(bas)
            n = -n
        while n:
            if n & 1:
                res = self.sqrt_prod(res, bas)
            bas = self.sqrt_prod(bas, bas)
            n >>= 1
        return res
    def sqrt_frac(self, s1, s2):
        s1 = self.trim_sqrt(s1)
        return self.sqrt_prod(s1, sqrt_inv(s2))
