class NTT:
    def __init__(self, convolution_rank=1, binary_level=27, modulo_minimum=1):
        self.cr = convolution_rank
        self.bl = binary_level
        self.modulo_minimum = modulo_minimum
        self.modulo_list = [1]*convolution_rank
        self.primitive_root_list = [1]*convolution_rank
        self.bin_list = [1]*(binary_level+1)
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
        bas = 1
        r = 0
        for i in range(num):
            x, y = self.extgcd(bas, -m_list[i], a_list[i]-r)
            if x < 0:
                return -1
            r += bas * x
            bas *= m_list[i]
        return r % bas
    def inved(self, a, modulo):
        x, y, u, v, k, l = 1, 0, 0, 1, a, modulo
        while l:
            x, y, u, v, k, l = u, v, x - u * (k // l), y - v * (k // l), l, k % l
        return x%modulo
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
    def simply_ntt(self, f, n, MOD, root):
        if n == 1:
            return f
        depth = len(bin(n))-3
        res = [0]*n
        res[0] = f[0]
        pos = 0
        for i in range(1, n):
            pnt = n >> 1
            c = pnt
            while pos & pnt:
                pnt >>= 1
                c += pnt
            pos ^= c
            res[i] = f[pos]
        left = 2
        right = 1
        thgir = 1 << (depth - 1)
        base_list = [1]*(self.bl+1)
        base_list[-1] = self.inved(root, MOD)
        for i in range(self.bl, 0, -1):
            base_list[i-1] = base_list[i] * base_list[i] % MOD
        for i in range(depth):
            grow = 1
            seed = base_list[i+1]
            for k in range(right):
                idx_l = k
                idx_r = k + right
                for j in range(thgir):
                    u = res[idx_l]
                    v = res[idx_r] * grow % MOD
                    res[idx_l] = (u + v) % MOD
                    res[idx_r] = (u - v) % MOD
                    idx_l += left
                    idx_r += left
                grow *= seed
                grow %= MOD
            left <<= 1
            right <<= 1
            thgir >>= 1
        return res
    def inverse_ntt(self, f, n, MOD, root):
        res = self.simply_ntt(f, n, MOD, self.inved(root, MOD))
        ipl = self.inved(n, MOD)
        for i in range(n):
            res[i] *= ipl
            res[i] %= MOD
        return res
