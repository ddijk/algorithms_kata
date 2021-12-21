def even_only(a):
    
    if not len(a):
        return []

    if a[0] % 2 == 0:
        res = even_only(a[1:])
        res.append(a[0])
        return res
    else:
        return even_only(a[1:] )
