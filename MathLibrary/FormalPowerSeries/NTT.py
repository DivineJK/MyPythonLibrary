class NTT:
    def __init__(self, convolution_rank=1, binary_level=27, modulo_minimum=1):
        self.cr = convolution_rank
        self.bl = binary_level
        self.modulo_minimum = modulo_minimum
        self.modulo_list = [1]*convolution_rank
        self.primitive_root_list = [1]*convolution_rank
        self.bin_list = [1]*(binary_level+1)
        self.primitive_base_matrix = [[0]*(binary_level+1) for __ in range(convolution_rank)]
        self.inverse_base_matrix = [[0]*(binary_level+1) for __ in range(convolution_rank)]
        for i in range(binary_level):
            self.bin_list[i+1] = self.bin_list[i] << 1
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
        if b == 0:
            if a == 0:
                if c == 0:
                    return 0, 0
                return -1, -1
            if c % a == 0:
                return c // a, 0
            return -1, -1
        if b < 0:
            a, b, c = -a, -b, -c
        tk, tl = a, b
        while tl:
            tk, tl = tl, tk % tl
        if c % tk:
            return -1, -1
        a //= tk
        b //= tk
        c //= tk
        x, y, u, v, k, l = 1, 0, 0, 1, a, b
        while l:
            x, y, u, v = u, v, x - u * (k // l), y - v * (k // l)
            k, l = l, k % l
        x = c*x % b
        y = (c-a*x)//b
        return x, y
    def CRT(self, num, a_list, m_list):
        for i in range(num):
            x, y = self.extgcd(bas, -m_list[i], a_list[i]-r)
            if x < 0:
                return -1
            r += bas * x
            bas *= m_list[i]
        return r % bas
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
                    if pow(r, self.bin_list[j], self.modulo_list[i]) == 1:
                        fflg = False
                        break
                if pow(r, self.bin_list[-1], self.modulo_list[i]) != 1:
                    fflg = False
                if fflg:
                    flg = False
                else:
                    r += 1
                    if r >= self.modulo_list[i]:
                        break
            self.primitive_root_list[i] = r
    def make_primitive_root(self):
        cnt = 0
        last = self.bin_list[-1]
        j = (self.modulo_minimum-1) // last
        if j % 2 == 0:
            j += 1
        while cnt < self.cr:
            if self.IsPrime(j*last+1):
                flg = True
                r = 1
                while flg:
                    fflg = True
                    for i in range(self.bl):
                        if pow(r, self.bin_list[i], j*last+1) == 1:
                            fflg = False
                            break
                    if pow(r, last, j*last+1) != 1:
                        fflg = False
                    if fflg:
                        flg = False
                    else:
                        r += 1
                        if r >= j*last+1:
                            break
                if flg==False:
                    self.modulo_list[cnt] = j*last+1
                    self.primitive_root_list[cnt] = r
                    cnt += 1
            j += 2
    def make_basis(self):
        for i in range(self.cr):
            for j in range(self.bl):
                tmp = pow(2, self.bl-j)
                self.primitive_base_matrix[i][j] = pow(self.primitive_root_list[i], tmp, self.modulo_list[i])
                self.inverse_base_matrix[i][j] = self.inved(self.primitive_base_matrix[i][j], self.modulo_list[i])
    def simply_ntt(self, f, idx, inverse=False):
        fl = len(f)
        n = 1
        depth = 0
        while n < fl:
            n <<= 1
            depth += 1
        res = [0]*n
        tmp = [0]*n
        MOD = self.modulo_list[idx]
        ipl = self.inved(n, MOD)
        for i in range(n):
            bas = 1
            pos = 0
            for j in range(depth, 0, -1):
                pos += bas * ((i>>(j-1)) & 1)
                bas <<= 1
            res[i] = f[pos]
        left = 2
        right = 1
        thgir = 1 << (depth - 1)
        for i in range(depth):
            grow = 1
            seed = self.inverse_base_matrix[idx][i+1]
            if inverse:
                seed = self.primitive_base_matrix[idx][i+1]
            for k in range(right):
                for j in range(thgir):
                    idx_l = j*left+k
                    idx_r = j*left+k+right
                    tmp[idx_l] = (res[idx_l] + grow * res[idx_r]) % MOD
                    tmp[idx_r] = (res[idx_l] - grow * res[idx_r]) % MOD
                grow *= seed
                grow %= MOD
            left <<= 1
            right <<= 1
            thgir >>= 1
            for j in range(n):
                res[j] = tmp[j]
        if inverse:
            for i in range(n):
                res[i] *= ipl
                res[i] %= MOD
        return res
