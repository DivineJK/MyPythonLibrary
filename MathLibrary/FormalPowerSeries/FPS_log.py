def fps_logarithm(f, MOD=MOD_free):
    n = len(f)
    bin_top = 1
    while bin_top < n:
        bin_top <<= 1
    x = f[:] + [0]*(bin_top-n)
    df = differentiate(x, MOD)
    inv_f = inverse(x)
    x = convolute_one(df, inv_f)
    return integrate(x, MOD)
