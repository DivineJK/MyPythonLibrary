class IntLib:
    def __init__(self, convolution_rank, binary_level):
        self.cr = convolution_rank
        self.bl = binary_level
        self.fact_cnt = 0
        self.fact = [1]
        self.invf = [1]
        self.modulo_list = [1]*convolution_rank
        self.primal_root_list = [1]*convolution_rank
        self.bin_list = [1]*(binary_level+1)
        self.primal_base_matrix = [[0 for _ in range(binary_level+1)] for __ in range(convolution_rank)]
        self.inverse_base_matrix = [[0 for _ in range(binary_level+1)] for __ in range(convolution_rank)]
        for i in range(binary_level):
            self.bin_list[i+1] = self.bin_list[i] * 2
    
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
            
    def inved(self, a, modulo):
        x, y = self.extgcd(a, modulo, 1)
        return (x+modulo)%modulo
    
    def make_fact(self, n, modulo):
        if n > self.fact_cnt:
            self.fact = self.fact[:] + [0]*(n-self.fact_cnt)
            self.invf = self.invf[:] + [0]*(n-self.fact_cnt)
            for i in range(self.fact_cnt, n):
                self.fact[i+1] = self.fact[i] * (i + 1)
                self.fact[i+1] %= modulo
            self.invf[-1] = self.inved(self.fact[-1], modulo)
            for i in range(n, self.fact_cnt, -1):
                self.invf[i-1] = self.invf[i] * i
                self.invf[i-1] %= modulo
            self.fact_cnt = n
            
    def root_manual(self):
        for i in range(self.cr):
            r = 1
            flg = True
            while flg:
                fflg = True
                for j in range(self.bl):
                    if self.doubling(r, self.bin_list[j], self.modulo_list[i]) == 1:
                        fflg = False
                if self.doubling(r, self.bin_list[-1], self.modulo_list[i]) != 1:
                    fflg = False
                if fflg:
                    flg = False
                else:
                    r += 1
                    if r >= self.modulo_list[i]:
                        break
            self.primal_root_list[i] = r
    
    def make_prime_root(self):
        cnt = 0
        j = 1
        last = self.bin_list[-1]
        while cnt < self.cr:
            if self.IsPrime(j*last+1):
                flg = True
                r = 1
                while flg:
                    fflg = True
                    for i in range(self.bl):
                        if self.doubling(r, self.bin_list[i], j*last+1) == 1:
                            fflg = False
                    if self.doubling(r, last, j*last+1) != 1:
                        fflg = False
                    if fflg:
                        flg = False
                    else:
                        r += 1
                        if r >= j*last+1:
                            break
                if flg==False:
                    self.modulo_list[cnt] = j*last+1
                    self.primal_root_list[cnt] = r
                    cnt += 1
            j += 2
    
    def make_basis(self):
        for i in range(self.cr):
            for j in range(self.bl):
                tmp = self.doubling(2, self.bl-j)
                self.primal_base_matrix[i][j] = self.doubling(self.primal_root_list[i], tmp, self.modulo_list[i])
                self.inverse_base_matrix[i][j] = self.inved(self.primal_base_matrix[i][j], self.modulo_list[i])
    
    def NTT(self, f, n, idx, depth, inverse=False, surface=True):
        res = [0 for _ in range(n)]
        tmp = [0 for _ in range(n)]
        MOD = self.modulo_list[idx]
        ipl = self.inved(n, MOD)
        for i in range(n):
            bas = 1
            pos = 0
            for j in range(depth, 0, -1):
                pos += bas * ((i>>(j-1)) % 2)
                bas *= 2
            res[i] = f[pos]
        for i in range(depth):
            grow = 1
            seed = inverse * self.primal_base_matrix[idx][i+1] + (1 - inverse) * self.inverse_base_matrix[idx][i+1]
            for k in range(1<<i):
                for j in range(1<<(depth-i-1)):
                    tmp[j*(1<<(i+1))+k+0*(1<<i)] = (res[j*(1<<(i+1))+k] + grow * res[j*(1<<(i+1))+k+(1<<i)]) % MOD
                    tmp[j*(1<<(i+1))+k+1*(1<<i)] = (res[j*(1<<(i+1))+k] - grow * res[j*(1<<(i+1))+k+(1<<i)]) % MOD
                grow *= seed
                grow %= MOD
            for j in range(n):
                res[j] = tmp[j]
        if inverse:
            for i in range(n):
                res[i] *= ipl
                res[i] %= MOD
        return res
    
    def frac_sum(self, f1, f2, weight=1):
        if f1[1] == 0 or f2[1] == 0:
            raise ValueError("Division by zero. f1 = {}/{}, f2 = {}/{}".format(f1[0], f1[1], f2[0], f2[1])) from None
        f = [f1[0]*f2[1]+weight*f2[0]*f1[1], f1[1]*f2[1]]
        g = self.gcd(f[0], f[1])
        f[0] //= g
        f[1] //= g
        return f
    
    def frac_prod(self, f1, f2, inverse=False):
        if inverse:
            f = [f1[0]*f2[1], f1[1]*f2[0]]
        else:
            f = [f1[0]*f2[0], f1[1]*f2[1]]
        if f[1] == 0:
            raise ValueError("Division by zero. f1 = {}/{}, f2 = {}/{}".format(f1[0], f1[1], f2[0], f2[1])) from None
        g = self.gcd(f[0], f[1])
        f[0] //= g
        f[1] //= g
        return f
