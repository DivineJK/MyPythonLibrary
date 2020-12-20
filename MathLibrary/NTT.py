class NTT:
    def __init__(self, convolution_rank=1, binary_level=27):
        self.cr = convolution_rank
        self.bl = binary_level
        self.modulo_list = [1]*convolution_rank
        self.primal_root_list = [1]*convolution_rank
        self.bin_list = [1]*(binary_level+1)
        self.primal_base_matrix = [[0]*(binary_level+1) for __ in range(convolution_rank)]
        self.inverse_base_matrix = [[0]*(binary_level+1) for __ in range(convolution_rank)]
        for i in range(binary_level):
            self.bin_list[i+1] = self.bin_list[i] * 2
    def extgcd(self, a, b, c):
        if b < 0:
            a, b, c = -a, -b, -c
        tk, tl = a, b
        while tl:
            tk, tl = tl, tk % tl
        if c % k:
            return "No Solution"
        a //= tk
        b //= tk
        c //= tk
        x, y, u, v, k, l = 1, 0, 0, 1, a, b
        while l:
            x, y, u, v = u, v, x - u * (k // l), y - v * (k // l)
            k, l = l, k % l
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
    def inved(self, a, modulo):
        x, y = self.extgcd(a, modulo, 1)
        return (x+modulo)%modulo
    def make_fact(self, n, modulo):
        if modulo != self.prev_mod:
            self.fact_cnt = 0
            self.fact = [1]
            self.invf = [1]
            self.bernouill_cnt = 0
            self.bernouill = [1]
        self.prev_mod = modulo
        if n > self.fact_cnt:
            self.fact = self.fact[:] + [0]*(n-self.fact_cnt)
            self.invf = self.invf[:] + [0]*(n-self.fact_cnt)
            for i in range(self.fact_cnt, n):
                self.fact[i+1] = self.fact[i] * (i + 1)
                if modulo:
                    self.fact[i+1] %= modulo
            if modulo:
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
                        break
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
                            break
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
    def simply_ntt(self, f, n, idx, depth, inverse=False, surface=True):
        res = [0]*n
        tmp = [0]*n
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
