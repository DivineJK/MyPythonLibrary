def string_decimal(s):
    if '.' in s:
        pnt = -1
        while s[pnt] != '.':
            pnt -= 1
        pnt += 1
        if pnt == 0:
            return (int(s[:pnt-1]), pnt)
        return (int(s[:pnt-1]+s[pnt:]), pnt)
    return (int(s), 0)
