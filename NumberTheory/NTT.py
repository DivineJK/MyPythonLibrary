class NTT:
    def __init__(self, convolution_rank, binary_level):
        self.cr = convolution_rank
        self.bl = binary_level
        self.modulo_list = [1]*convolution_rank
        self.primal_root_list = [1]*convolution_rank
        self.bin_list = [1]*(binary_level+1)
        self.primal_base_matrix = [[0 for _ in range(binary_level+1)] for __ in range(convolution_rank)]
        self.inverse_base_matrix = [[0 for _ in range(binary_level+1)] for __ in range(convolution_rank)]
        for i in range(binary_level):
            self.bin_list[i+1] = self.bin_list[i] * 2
    
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
    
    def extgcd(self, a, b, c):
        x, y, u, v, k, l = 1, 0, 0, 1, a, b
        while l:
            x, y, u, v = u, v, x - u * (k // l), y - v * (k // l)
            k, l = l, k % l
        if c % k:
            return "No Solution"
        return x * c, y * c
    
    def inved(self, a, modulo):
        x, y = self.extgcd(a, modulo, 1)
        return (x+modulo)%modulo
    
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
        mod = self.modulo_list[idx]
        if n == 1:
            return f
        if n == 2:
            xf = [(f[0] + f[1])%mod, (f[0] - f[1])%mod]
            if inverse * surface:
                xf[0] *= self.inved(2, mod)
                xf[0] %= mod
                xf[1] *= self.inved(2, mod)
                xf[1] %= mod
            return xf
        hn = n // 2
        fe = [f[2*i+0] for i in range(hn)]
        fo = [f[2*i+1] for i in range(hn)]
        fe = self.NTT(fe, hn, idx, depth-1, inverse, False)
        fo = self.NTT(fo, hn, idx, depth-1, inverse, False)
        xf = [0 for _ in range(n)]
        grow = 1
        if inverse:
            seed = self.primal_base_matrix[idx][depth]
        else:
            seed = self.inverse_base_matrix[idx][depth]
        for i in range(hn):
            right = (fo[i] * grow) % mod
            xf[i+0*hn] = (fe[i] + right) % mod
            xf[i+1*hn] = (fe[i] - right) % mod
            grow *= seed
            grow %= mod
        if inverse * surface:
            invn = self.inved(n, mod)
            for i in range(n):
                xf[i] *= invn
                xf[i] %= mod
        return xf
    
    def CRT(self, num, a_list, m_list):
        r = a_list[0]
        bas = m_list[0]
        x, y = 0, 0
        for i in range(1, num):
            x, y = self.extgcd(bas, -m_list[i], -a_list[i]-r)
            r += bas * x
            bas *= b[i]
        return r % bas
