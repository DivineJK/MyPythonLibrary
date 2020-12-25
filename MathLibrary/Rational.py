from IntLib import IntLib

IL = IntLib()

class Rational:
    def __init__(self):
        self.bernouill_cnt = 0
        self.bernouill = [[1, 1]]
    def frac_sum(self, f1, f2, weight=1):
        if f1[1] == 0 or f2[1] == 0:
            raise ValueError("Division by zero. f1 = {}/{}, f2 = {}/{}".format(f1[0], f1[1], f2[0], f2[1])) from None
        f = [f1[0]*f2[1]+weight*f2[0]*f1[1], f1[1]*f2[1]]
        g = IL.gcd(f[0], f[1])
        f[0] //= g
        f[1] //= g
        if f[1] < 0:
            f[0] = -f[0]
            f[1] = -f[1]
        return f
    
    def frac_prod(self, f1, f2, inverse=False):
        if inverse:
            f = [f1[0]*f2[1], f1[1]*f2[0]]
        else:
            f = [f1[0]*f2[0], f1[1]*f2[1]]
        if f[1] == 0:
            raise ValueError("Division by zero. f1 = {}/{}, f2 = {}/{}".format(f1[0], f1[1], f2[0], f2[1])) from None
        g = IL.gcd(f[0], f[1])
        f[0] //= g
        f[1] //= g
        if f[1] < 0:
            f[0] = -f[0]
            f[1] = -f[1]
        return f
    
    def get_bernouill(self, n):
        IL.make_fact(n+1)
        if n > IL.bernouill_cnt:
            for i in range(self.bernouill_cnt, n):
                IL.bernouill.append([0, 1])
            for i in range(self.bernouill_cnt+1, n+1):
                if i % 2 == 0:
                    for j in range(i):
                        if j == 1 or j % 2 == 0:
                            tmp = self.frac_sum([0, 1], [-IL.fact[i], IL.fact[i-j+1]*IL.fact[j]])
                            self.bernouill[i] = self.frac_sum(self.bernouill[i], self.frac_prod(self.bernouill[j], tmp))
            self.bernouill_cnt = n
        return self.bernouill[n]
