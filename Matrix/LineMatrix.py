class line_matrix:
    def verify(self, a):
        if len(a) < 2:
            return False
        h, w = a[-2], a[-1]
        if h*w != len(a) - 2:
            return False
        return True
    def identity(self, n):
        res = [0]*(n*n+2)
        res[-2] = n
        res[-1] = n
        for i in range(n):
            res[i*(n+1)] = 1
        return res
    def zeros(self, n, m):
        res = [0]*(n*m+2)
        res[-2] = n
        res[-1] = m
        return res
    def mat_sum(self, a, b, weight=1, modulo=0):
        if not (self.verify(a) and self.verify(b)):
            raise RuntimeError("invalid arguments: matrix") from None
        if len(a) != len(b):
            raise RuntimeError("invalid arguments: size") from None
        n1, m1 = a[-2], a[-1]
        n2, m2 = b[-2], b[-1]
        if n1 != n2 or m1 != m2:
            raise RuntimeError("invalid arguments: size") from None
        res = self.zeros(n1, m1)
        for i in range(n1*m1+2):
            res[i] = a[i] + weight*b[i]
            if modulo:
                res[i] %= modulo
        return res
    def mat_prod(self, a, b, modulo=0):
        if not (self.verify(a) and self.verify(b)):
            raise RuntimeError("invalid arguments: matrix") from None
        n1, m1 = a[-2], a[-1]
        n2, m2 = b[-2], b[-1]
        if m1 != n2:
            raise RuntimeError("invalid arguments: size") from None
        res = self.zeros(n1, m1)
        for i in range(n1*m2):
            x, y = (i//m2)*m1, i%m2
            for k in range(m1):
                res[i] += a[x]*b[y]
                if modulo:
                    res[i] %= modulo
                x += 1
                y += m2
        return res
    def mat_pow(self, a, n, modulo=0):
        if not self.verify(a):
            raise RuntimeError("invalid arguments: matrix") from None
        if a[-1] != a[-2]:
            raise RuntimeError("invalid arguments: size") from None
        res = self.identity(a[-1])
        bas = a[:]
        while n:
            if n & 1:
                res = self.mat_prod(res, bas, modulo)
            bas = self.mat_prod(bas, bas, modulo)
            n >>= 1
        return res
