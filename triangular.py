def triangular(n):
    return prim(n)[-1]

def prim(n):
    
    if n == 0:
        return []

    if n ==1:
        return [1]

    res = prim(n-1)
    res.append(len(res)+1+res[-1])
    return res
