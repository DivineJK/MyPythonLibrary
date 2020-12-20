class IntLib:
    def __init__(self):
        self.prev_mod = 0
        self.fact_cnt = 0
        self.fact = [1]
        self.invf = [1]
        self.bernouill_cnt = 0
        self.bernouill = [1]
    def gcd(self, a, b):
        if a < 0:
            a = -a
            b = -b
        k, l = a, b
        while l:
            k, l = l, k % l
        return k
    def extgcd(self, a, b, c):
        if b < 0:
            a, b, c = -a, -b, -c
        x, y, u, v, k, l = 1, 0, 0, 1, a, b
        while l:
            x, y, u, v = u, v, x - u * (k // l), y - v * (k // l)
            k, l = l, k % l
        if c % k:
            return "No Solution"
        return x * c, y * c
    def CRT(self, num, a_list, m_list):
        r = a_list[0]
        bas = m_list[0]
        x, y = 0, 0
        for i in range(1, num):
            x, y = self.extgcd(bas, -m_list[i], a_list[i]-r)
            r += bas * x
            bas *= m_list[i]
        return r % bas
    def doubling(self, n, m, modulo=0):
        y = 1
        tmp = m
        bas = n
        while tmp:
            if tmp % 2:
                y *= bas
                if modulo:
                    y %= modulo
            bas *= bas
            if modulo:
                bas %= modulo
            tmp >>= 1
        return y
    def powlimit(self, n):
        y = 1
        cnt = 0
        while y < n:
            y *= 2
            cnt += 1
        return y, cnt
    def IsPrime(self, num):
        p = 2
        if num <= 1:
            return False
        while p * p <= num:
            if num % p == 0:
                return False
            p += 1
        return True
    def factorization(self, n, easy=False):
        a = n
        D = []
        p = 2
        cnt = 0
        while a % p == 0:
            a //= p
            cnt += 1
        if cnt:
            if easy:
                D.append(p)
            else:
                D.append([p, cnt])
        p += 1
        while a != 1:
            cnt = 0
            while a % p == 0:
                cnt += 1
                a //= p
            if cnt:
                if easy:
                    D.append(p)
                else:
                    D.append([p, cnt])
            p += 2
            if p * p > n and a != 1:
                if easy:
                    D.append(a)
                else:
                    D.append([a, 1])
                break
        return D
    def totient(self, n):
        d = self.factorization(n, True)
        res = n
        for i in d:
            res //= i
            res *= i - 1
        return res
    def divisors(self, n, ordered=False):
        res = [1]
        D = self.factorization(n)
        cnt = 1
        for i in D:
            tmp = i[0]
            for j in range(i[1]):
                for k in range(cnt):
                    res.append(tmp*res[k])
                tmp *= i[0]
            cnt *= (i[1] + 1)
        if ordered:
            res.sort()
        return res
    def get_bernouill(self, n, modulo):
        if modulo <= 0 or not self.IsPrime(modulo):
            raise RuntimeError("modulo value is invalid") from None
        if n+1 > self.fact_cnt:
            self.make_fact(n+1, modulo)
        if n > self.bernouill_cnt:
            for i in range(self.bernouill_cnt, n):
                self.bernouill.append(0)
            for i in range(self.bernouill_cnt+1, n+1):
                if i % 2 == 0 or i == 1:
                    for j in range(i):
                        if j == 1 or j % 2 == 0:
                            tmp = self.invf[i-j+1]*self.invf[j] % modulo
                            self.bernouill[i] += self.bernouill[j]*tmp%modulo
                            self.bernouill[i] %= modulo
                    self.bernouill[i] *= -self.fact[i]
                    self.bernouill[i] %= modulo
            self.bernouill_cnt = n
        return self.bernouill[n]
    def power_sum(self, n, m, modulo):
        bas = n
        if modulo <= 0 or not self.IsPrime(modulo):
            raise RuntimeError("modulo value is invalid") from None
        S = 0
        sign = 1 - 2 * (m % 2)
        for i in range(m+1):
            if m-i > self.bernouill_cnt:
                B = self.get_bernouill(m-i, modulo)
            else:
                B = self.bernouill[m-i]
            S += (self.invf[i+1]*self.invf[m-i]%modulo)*(sign*B*bas%modulo)%modulo
            S %= modulo
            bas *= n
            bas %= modulo
            sign *= -1
        return S * self.fact[m] % modulo
