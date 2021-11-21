def CRT(num, a_list, m_list):
    for i in range(num):
        x, y = extgcd(bas, -m_list[i], a_list[i]-r)
        if x < 0:
            return -1
        r += bas * x
        bas *= m_list[i]
    return r % bas
