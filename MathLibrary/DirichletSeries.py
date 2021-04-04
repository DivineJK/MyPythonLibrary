class dirichlet_series:
    def __init__(self):
        self.totient_n = 0
        self.totient_list = []
        self.totient_sum = []
        self.totient_sum_dict = {}
    def FMT(self, f):
        n = len(f)
        p_flg = [True]*(n+1)
        p_flg[0] = False
        p_flg[1] = False
        p_tab = []
        if n == 2:
            p_tab.append(2)
        else:
            p = 3
            while p * p <= n:
                if p_flg[p]:
                    for i in range(p, n//p+1, 2):
                        p_flg[p*i] = False
                p += 1
            p_tab = [2]
            for i in range(3, n+1, 2):
                if p_flg[i]:
                    p_tab.append(i)
        res = [f[i] for i in range(n)]
        for i in p_tab:
            for j in range(n//i, 0, -1):
                res[i*j-1] -= res[j-1]
        return res
    def FZT(self, f):
        n = len(f)
        p_flg = [True]*(n+1)
        p_flg[0] = False
        p_flg[1] = False
        p_tab = []
        if n == 2:
            p_tab.append(2)
        else:
            p = 3
            while p * p <= n:
                if p_flg[p]:
                    for i in range(p, n//p+1, 2):
                        p_flg[p*i] = False
                p += 1
            p_tab = [2]
            for i in range(3, n+1, 2):
                if p_flg[i]:
                    p_tab.append(i)
        res = [f[i] for i in range(n)]
        for i in p_tab:
            for j in range(1, n//i+1):
                res[i*j-1] += res[j-1]
        return res
    def make_totient_list(self, n, modulo=0):
        self.totient_n = n
        self.totient_list = self.FMT([i+1 for i in range(n)])
        self.totient_sum = [1]*n
        for i in range(1, n):
            self.totient_sum[i] = self.totient_sum[i-1] + self.totient_list[i]
            if modulo:
                self.totient_sum[i] %= modulo
    def sum_of_totient(self, n, modulo=0):
        if n <= self.totient_n:
            return self.totient_sum[n-1]
        if n in self.totient_sum_dict:
            return self.totient_sum_dict[n]
        S = n * (n + 1) // 2 - (n - n//2) * self.sum_of_totient(1, modulo)
        if modulo:
            S %= modulo
        i = 2
        prev = n
        while i * i <= n:
            S -= (n//i - n//(i+1)) * self.sum_of_totient(i, modulo)
            if modulo:
                S %= modulo
            if i == n // i:
                i += 1
                break
            S -= self.sum_of_totient(n//i, modulo)
            if modulo:
                S %= modulo
            i += 1
        self.totient_sum_dict[n] = S
        return S
