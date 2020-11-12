class matrix_collections:
    def __init__(self, additional_type=set()):
        self.number_type = {int, float}
        for i in additional_type:
            self.number_type.add(i)
    def zeros(self, n, m):
        return [[0]*m for _ in range(n)]
    def identity(self, n):
        return [[i==j for j in range(n)] for i in range(n)]
    def inved(self, a, modulo):
        x, y, u, v, k, l = 1, 0, 0, 1, a, modulo
        while l:
            x, y, u, v, k, l = u, v, x - u * (k // l), y - v * (k // l), l, k % l
        return x % modulo
    def ismatrix(self, a):
        if type(a) != list:
            return False
        n = len(a)
        flg = True
        for i in range(n):
            if type(a[i]) != list:
                return False
        m = len(a[0])
        for i in range(n):
            if len(a[i]) != m:
                flg = False
                break
            for j in range(m):
                if type(a[i][j]) not in self.number_type:
                    flg = False
                    break
            if not flg:
                break
        return flg
    def mat_sum(self, a, b, weight=1, modulo=0):
        if not (self.ismatrix(a) and self.ismatrix(b)):
            raise Exception("strange input{}: a = {}, b = {}".format('s'*(self.ismatrix(a)+self.ismatrix(b)==0), a, b))
        if len(a) != len(b) or len(a[0]) != len(b[0]):
            raise Exception("sizes of matrices are invalid for matrix summation")
        n, m = len(a), len(a[0])
        res = self.zeros(n, m)
        for i in range(n):
            for j in range(m):
                res[i][j] = a[i][j] + weight*b[i][j]
                if modulo:
                    res[i][j] %= modulo
        return res
    def mat_prod(self, a, b, modulo=0):
        if not (self.ismatrix(a) and self.ismatrix(b)):
            raise Exception("strange input{}: a = {}, b = {}".format('s'*(self.ismatrix(a)+self.ismatrix(b)==0), a, b))
        if len(a[0]) != len(b):
            raise Exception("sizes of matrices are invalid for matrix product")
        n, l, m = len(a), len(a[0]), len(b[0])
        res = self.zeros(n, m)
        for i in range(n):
            for j in range(m):
                for k in range(l):
                    res[i][j] += a[i][k] * b[k][j]
                    if modulo:
                        res[i][j] %= modulo
        return res
    def mat_inv(self, a, modulo=0):
        if not self.ismatrix(a):
            raise Exception("strange input: a = {}".format(a))
        if len(a[0]) != len(a):
            raise Exception("sizes of matrices are invalid for matrix inverse")
        n = len(a)
        mid = self.zeros(n, 2*n)
        for i in range(n):
            mid[i][i+n] = 1
            for j in range(n):
                if modulo and type(mid[i][j]) != int:
                    raise Exception("value error: mid[{}][{}] = {}".format(i, j, mid[i][j]))
                mid[i][j] = a[i][j]
                if modulo:
                    mid[i][j] %= modulo
        for i in range(n):
            pnt = i
            while mid[pnt][i] == 0:
                pnt += 1
                if pnt == n:
                    raise ZeroDivisionError()
            for j in range(2*n):
                mid[i][j], mid[pnt][j] = mid[pnt][j], mid[i][j]
            tmp = mid[i][i]
            if modulo:
                tmp = self.inved(mid[i][i], modulo)
            for j in range(i, 2*n):
                if modulo:
                    mid[i][j] *= tmp
                    mid[i][j] %= modulo
                else:
                    mid[i][j] /= tmp
            for j in range(i+1, n):
                tmp1 = mid[j][i]
                for k in range(i, 2*n):
                    if modulo:
                        mid[j][k] -= tmp1 * mid[i][k]
                        mid[j][k] %= modulo
                    else:
                        mid[j][k] -= tmp1 * mid[i][k]
        for i in range(n-1, 0, -1):
            for j in range(i, 0, -1):
                tmp1 = mid[j-1][i]
                for k in range(i, 2*n):
                    if modulo:
                        mid[j-1][k] -= tmp1 * mid[i][k]
                        mid[j-1][k] %= modulo
                    else:
                        mid[j-1][k] -= tmp1 * mid[i][k]
        res = [[mid[i][j+n] for j in range(n)] for i in range(n)]
        return res
    def mat_pow(self, a, m, modulo=0):
        if not self.ismatrix(a):
            raise Exception("strange input: a = {}".format(a))
        if len(a[0]) != len(a):
            raise Exception("size of matrix is invalid for matrix power")
        n = len(a)
        res = self.identity(n)
        bas = [[a[i][j] for j in range(n)] for i in range(n)]
        if m < 0:
            m = -m
            bas = self.mat_inv(bas, modulo)
        tmp = m
        while tmp:
            if tmp & 1:
                res = self.mat_prod(res, bas, modulo)
            bas = self.mat_prod(bas, bas, modulo)
            tmp >>= 1
        return res
    def kronecker_product(self, a, b, modulo=0):
        if not (self.ismatrix(a) and self.ismatrix(b)):
            raise Exception("strange input{}: a = {}, b = {}".format('s'*(self.ismatrix(a)+self.ismatrix(b)==0), a, b))
        n, m, p, q = len(a), len(a[0]), len(b), len(b[0])
        res = self.zeros(n*p, m*q)
        for i in range(n*p):
            for j in range(m*q):
                res[i][j] = a[i//p][j//q] * b[i%p][j%q]
                if modulo:
                    if type(res[i][j]) != int:
                        raise Exception("value error: res[{}][{}] = {}".format(i, j, res[i][j]))
                    res[i][j] %= modulo
        return res
