max_fact = 500000
mod = 998244353
fact = [1]*(max_fact+1)
invf = [1]*(max_fact+1)
invn = [1]*(max_fact+1)
for i in range(max_fact):
    fact[i+1] = (i+1) * fact[i] % mod
    if i:
        invn[i+1] = mod-(mod//(i+1))*invn[mod%(i+1)]%mod
        invf[i+1] = invf[i]*invn[i+1]%mod
