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
    def determinant(self, a, modulo=0):
        if not self.ismatrix(a):
            raise Exception("strange input: a = {}".format(a))
        if len(a[0]) != len(a):
            raise Exception("size of matrix is invalid for matrix power")
        n = len(a)
        mid = self.zeros(n, n)
        res = 1
        for i in range(n):
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
                    res = 0
                    break
            if res == 0:
                break
            if i != pnt:
                if modulo:
                    res *= modulo - 1
                    res %= modulo
                else:
                    res *= -1
            for j in range(n):
                mid[i][j], mid[pnt][j] = mid[pnt][j], mid[i][j]
            tmp = mid[i][i]
            res *= tmp
            if modulo:
                res %= modulo
                tmp = self.inved(mid[i][i], modulo)
            for j in range(i, n):
                if modulo:
                    mid[i][j] *= tmp
                    mid[i][j] %= modulo
                else:
                    mid[i][j] /= tmp
            for j in range(i+1, n):
                tmp1 = mid[j][i]
                for k in range(i, n):
                    if modulo:
                        mid[j][k] -= tmp1 * mid[i][k]
                        mid[j][k] %= modulo
                    else:
                        mid[j][k] -= tmp1 * mid[i][k]
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
    def linear_equation_solver(self, a, b, modulo=0):
        if not self.ismatrix(a):
            raise Exception("strange input: a = {}".format(a))
        if type(b) != list:
            raise Exception("strange input: b = {}".format(b))
        for i in b:
            if type(i) not in self.number_type:
                raise Exception("strange input: b = {}".format(b))
        n, m, p = len(a), len(a[0]), len(b)
        ext_mat = self.zeros(n, m+1)
        for i in range(n):
            for j in range(m):
                ext_mat[i][j] = a[i][j]
                if modulo: ext_mat[i][j] %= modulo
        if m < p:
            for i in range(m, p):
                ext_mat.append([0]*(m+1))
        for i in range(p):
            ext_mat[i][m] = b[i]
            if modulo: ext_mat[i][m] %= modulo
        pnt = 0
        for j in range(m):
            x = pnt
            flg = True
            while x < n:
                if ext_mat[x][j]:
                    flg = False
                    break
                x += 1
            if flg: continue
            if pnt != x:
                for k in range(j, m+1):
                    ext_mat[pnt][k], ext_mat[x][k] = ext_mat[x][k], ext_mat[pnt][k]
            tmp = ext_mat[pnt][j]
            ext_mat[pnt][j] = 1
            invt = 0
            if modulo:
                invt = self.inved(tmp, modulo)
            for k in range(j+1, m+1):
                if modulo:
                    ext_mat[pnt][k] = invt * ext_mat[pnt][k] % modulo
                else:
                    ext_mat[pnt][k] /= tmp
            for l in range(pnt+1, n):
                tmp = ext_mat[l][j]
                ext_mat[l][j] = 0
                if tmp == 0: continue
                for k in range(j+1, m+1):
                    ext_mat[l][k] -= tmp * ext_mat[pnt][k]
                    if modulo:
                        ext_mat[l][k] %= modulo
            pnt += 1
        b = -1
        for i in range(n, 0, -1):
            flg = True
            for j in range(m):
                if ext_mat[i-1][j] != 0:
                    flg = False
                    break
            if flg:
                if ext_mat[i-1][m] != 0:
                    return [[-1]*(m+1)]
            else:
                b = i - 1
                break
        solution = [[0]*m for _ in range(m-b)]
        idx = [1]*m
        fid = [1]*m
        for i in range(b, -1, -1):
            s = 0
            while ext_mat[i][s] == 0:
                s += 1
            solution[0][s] = ext_mat[i][m]
            idx[s] = 0
            fid[s] = 0
            for j in range(i):
                tmp = ext_mat[j][s]
                ext_mat[j][s] = 0
                for k in range(s+1, m+1):
                    ext_mat[j][k] -= ext_mat[i][k] * tmp
                    if modulo:
                        ext_mat[j][k] %= modulo
        if idx[0]:
            solution[idx[0]][0] = 1
        for i in range(m-1):
            idx[i+1] += idx[i]
            if fid[i+1]:
                solution[idx[i+1]][i+1] = 1
        for i in range(b+1):
            s = 0
            while ext_mat[i][s] == 0:
                s += 1
            for j in range(s+1, m):
                if fid[j]:
                    solution[idx[j]][s] = -ext_mat[i][j]
                    if modulo:
                        solution[idx[j]][s] %= modulo
        return solution
