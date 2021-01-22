class discrete_log:
    def __init__(self):
        self.prev_num = -1
        self.prev_mod = -1
        self.prev_sqrt = -1
        self.prev_inv = -1
        self.baby_dict = {}
    def gcd(self, x, y):
        while y:
            x, y = y, x % y
        return x
    def extgcd(self, a, b, c):
        if b == 0:
            if a == 0:
                if c == 0:
                    return 0, 0
                return None
            if c % a == 0:
                return c // a, 0
            return None
        if b < 0:
            a, b, c = -a, -b, -c
        tk, tl = a, b
        while tl:
            tk, tl = tl, tk % tl
        if c % tk:
            return None
        a //= tk
        b //= tk
        c //= tk
        x, y, u, v, k, l = 1, 0, 0, 1, a, b
        while l:
            x, y, u, v = u, v, x - u * (k // l), y - v * (k // l)
            k, l = l, k % l
        x *= c
        k = x // b
        x -= k * b
        y *= c
        y += k * a
        return x, y
    def inved(self, a, modulo):
        x = self.extgcd(a, modulo, 1)[0] % modulo
        return x
    def ext_inved(self, a, c, modulo):
        return self.extgcd(a, modulo, c)[0] % modulo
    def factorization(self, n):
        res = []
        cnt = 0
        a = n
        while a % 2 == 0:
            a //= 2
            cnt += 1
        if cnt:
            res.append([2, cnt])
        p = 3
        while a != 1:
            cnt = 0
            while a % p == 0:
                cnt += 1
                a //= p
            if cnt:
                res.append([p, cnt])
            p += 2
            if p * p > n and a != 1:
                res.append([a, 1])
                break
        return res
    def divisors(self, n):
        L = [1]
        p = 2
        c = 1
        while p * p <= n:
            if n % p == 0:
                c += 1
                L.append(p)
            p += 1
        for i in range(c, 0, -1):
            if L[i-1] * L[i-1] != n:
                L.append(n // L[i-1])
        return L
    def totient(self, n):
        a = n
        p = 2
        res = n
        while a != 1:
            if a % p == 0:
                res //= p
                res *= p - 1
                while a % p == 0:
                    a //= p
            p += 1
            if p * p > n and a != 1:
                res //= a
                res *= a - 1
                break
        return res
    def CRT(self, num, a_list, m_list):
        r = a_list[0]
        bas = m_list[0]
        x, y = 0, 0
        for i in range(1, num):
            x, y = self.extgcd(bas, -m_list[i], a_list[i]-r)
            r += bas * x
            bas *= m_list[i]
        return r % bas
    def generalized_bsgs(self, n, x, y):
        if x == 0:
            if y == 0:
                if n == 1:
                    return 0
                return 1
            if y == 1:
                if n == 1:
                    return -1
                return 0
            return -1
        fc = self.factorization(x)
        Mp = n
        tail = 0
        for i in fc:
            cnt = 0
            while Mp % i[0] == 0:
                Mp //= i[0]
                cnt += 1
            tail = max(tail, (i[1]+cnt-1)//i[1])
        fMp = self.totient(Mp)
        div_fMp = self.divisors(fMp)
        bas = 1
        for i in range(tail):
            if y == bas:
                return i
            bas *= x
            bas %= n
        loop = fMp
        for i, k in enumerate(div_fMp):
            if bas*pow(x, k, n)%n == bas:
                loop = k
                break
        b = self.prev_inv
        m = self.prev_sqrt
        e = pow(x, loop, n)
        if n != self.prev_sqrt or x != self.prev_num:
            self.baby_dict = {}
            self.prev_num = x
            self.prev_mod = n
            l, r = 0, loop
            m = (l + r) // 2
            while r - l > 1:
                if m * m <= loop:
                    l = m
                else:
                    r = m
                m = (l + r) // 2
            if m * m < loop:
                m += 1
            self.prev_sqrt = m
            b = pow(self.ext_inved(x, e, n), m, n)
            self.prev_inv = b
            f = bas
            for i in range(m):
                if f not in self.baby_dict:
                    self.baby_dict[f] = i
                f *= x
                f %= n
        g = y
        if y % self.gcd(bas, n) != 0:
            return -1
        for i in range(m):
            if g in self.baby_dict:
                return i * m + self.baby_dict[g] + tail
            g *= b
            g %= n
        return -1
dl = discrete_log()
T = int(input())
while T:
    T -= 1
    X, Y, M = map(int, input().split())
    print(dl.generalized_bsgs(M, X, Y))
