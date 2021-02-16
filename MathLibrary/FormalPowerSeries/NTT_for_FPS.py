class NTT_for_FPS:
    # mod = 998244353, root = 31, inverse_root = 128805723
    def ntt0(self, f, n, root=128805723):
        if n == 1:
            return f
        MOD = 998244353
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
        base_list = [1]*24
        base_list[-1] = root
        for i in range(23, 0, -1):
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
    def inverse_ntt0(self, f, n):
        res = self.ntt0(f, n, 31)
        MOD = 998244353
        x, y, u, v, k, l = 1, 0, 0, 1, n, MOD
        while l:
            x, y, u, v, k, l = u, v, x - u * (k // l), y - v * (k // l), l, k % l
        x %= MOD
        for i in range(n):
            res[i] *= x
            res[i] %= MOD
        return res
    # mod = 377487361, root = 197, inverse_root = 3832359
    def ntt1(self, f, n, root=3832359):
        if n == 1:
            return f
        MOD = 377487361
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
        base_list = [1]*24
        base_list[-1] = root
        for i in range(23, 0, -1):
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
    def inverse_ntt1(self, f, n):
        res = self.ntt1(f, n, 197)
        MOD = 377487361
        x, y, u, v, k, l = 1, 0, 0, 1, n, MOD
        while l:
            x, y, u, v, k, l = u, v, x - u * (k // l), y - v * (k // l), l, k % l
        x %= MOD
        for i in range(n):
            res[i] *= x
            res[i] %= MOD
        return res
    # mod = 595591169, root = 721, inverse_root = 72693513
    def ntt2(self, f, n, root=72693513):
        if n == 1:
            return f
        MOD = 595591169
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
        base_list = [1]*24
        base_list[-1] = root
        for i in range(23, 0, -1):
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
    def inverse_ntt2(self, f, n):
        res = self.ntt2(f, n, 721)
        MOD = 595591169
        x, y, u, v, k, l = 1, 0, 0, 1, n, MOD
        while l:
            x, y, u, v, k, l = u, v, x - u * (k // l), y - v * (k // l), l, k % l
        x %= MOD
        for i in range(n):
            res[i] *= x
            res[i] %= MOD
        return res
    # mod = 645922817, root = 19, inverse_root = 135983751
    def ntt3(self, f, n, root=135983751):
        if n == 1:
            return f
        MOD = 645922817
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
        base_list = [1]*24
        base_list[-1] = root
        for i in range(23, 0, -1):
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
    def inverse_ntt3(self, f, n):
        res = self.ntt3(f, n, 19)
        MOD = 645922817
        x, y, u, v, k, l = 1, 0, 0, 1, n, MOD
        while l:
            x, y, u, v, k, l = u, v, x - u * (k // l), y - v * (k // l), l, k % l
        x %= MOD
        for i in range(n):
            res[i] *= x
            res[i] %= MOD
        return res
    def convolute_one(self, f, g):
        n = len(f)
        m = len(g)
        bin_top = 1
        while bin_top < n + m:
            bin_top <<= 1
        if n * m <= 100000:
            res = [0]*bin_top
            for i in range(n):
                for j in range(m):
                    res[i+j] += (f[i] * g[j]) % 998244353
                    res[i+j] %= 998244353
            return res
        f = f[:] + [0]*(bin_top-n)
        g = g[:] + [0]*(bin_top-m)
        x = self.ntt0(f, bin_top)
        y = self.ntt0(g, bin_top)
        z = [x[i]*y[i]%998244353 for i in range(bin_top)]
        return self.inverse_ntt0(z, bin_top)
    def crt(self, a_list):
        m_list = (377487361, 595591169, 645922817)
        bas = 1
        r = 0
        for i in range(3):
            b = m_list[i]
            c = r-a_list[i]
            x, y, u, v, k, l = 1, 0, 0, 1, -bas, b
            while l:
                x, y, u, v, k, l = u, v, x - u * (k // l), y - v * (k // l), l, k % l
            x = c*x % b
            y = (c+bas*x)//b
            if x < 0:
                return -1
            r += bas * x
            bas *= m_list[i]
        return r % bas
    def convolute(self, f, g, modulo):
        n = len(f)
        m = len(g)
        bin_top = 1
        while bin_top < n + m:
            bin_top <<= 1
        if n * m <= 100000:
            res = [0]*bin_top
            for i in range(n):
                for j in range(m):
                    res[i+j] += (f[i] * g[j]) % modulo
                    res[i+j] %= modulo
            return res
        MOD1 = 377487361
        MOD2 = 595591169
        MOD3 = 645922817
        f = f[:] + [0]*(bin_top-n)
        g = g[:] + [0]*(bin_top-m)
        x = self.ntt1(f, bin_top)
        y = self.ntt1(g, bin_top)
        z1 = [x[i]*y[i]%MOD1 for i in range(bin_top)]
        z1 = self.inverse_ntt1(z1, bin_top)
        x = self.ntt2(f, bin_top)
        y = self.ntt2(g, bin_top)
        z2 = [x[i]*y[i]%MOD2 for i in range(bin_top)]
        z2 = self.inverse_ntt2(z2, bin_top)
        x = self.ntt3(f, bin_top)
        y = self.ntt3(g, bin_top)
        z3 = [x[i]*y[i]%MOD3 for i in range(bin_top)]
        z3 = self.inverse_ntt3(z3, bin_top)
        res = [self.crt((z1[i], z2[i], z3[i])) % modulo for i in range(bin_top)]
        return res
