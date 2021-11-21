# repunit: 拡張レピュニット数を求める。1をp-1個おきにl回繰り返した整数を計算する。
def repunit(p, l, modulo=0):
    res = 0
    bas = 1
    if modulo:
        bas = pow(10, p, modulo)
    else:
        bas = pow(10, p)
    rep_unit = 1
    while l:
        if l & 1:
            res *= bas
            res += rep_unit
            if modulo:
                res %= modulo
        rep_unit = (bas + 1) * rep_unit
        bas *= bas
        if modulo:
            rep_unit %= modulo
            bas %= modulo
        l >>= 1
    return res
