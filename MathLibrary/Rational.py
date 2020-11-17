from IntLib import IntLib as IL
class Rational:
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
