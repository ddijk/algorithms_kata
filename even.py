def even_only(a, result=[]):
    
    if not len(a):
        return result

    if a[0] % 2 == 0:
        result.append(a[0])

    return even_only(a[1:], result)
