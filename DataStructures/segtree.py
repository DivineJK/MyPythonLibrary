class segtree:
    def __init__(self, bin_level):
        self.bl = bin_level
        self.st = [[0 for __ in range(1<<_)] for _ in range(bin_level+1)]
    
    def st_make(self, n, arr):
        for j in range(n):
            tmp = j
            for i in range(self.bl, -1, -1):
                self.st[i][tmp] += arr[j]
                tmp >>= 1
    
    def st_add(self, i, p):
        tmp = i
        for i in range(self.bl, -1, -1):
            self.st[i][tmp] += p
            tmp >>= 1
    
    def st_sum(self, x):
        if x < 0:
            return 0
        S = 0
        pnt = 0
        b = 1 << (self.bl)
        for i in range(self.bl+1):
            pnt <<= 1
            if x >= b:
                S += self.st[i][pnt]
                pnt += 1
                x -= b
            b >>= 1
        return S
