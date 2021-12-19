def intersect(a,b):
    result = []
    a_dict = {e: True for e in a}
    [result.append(e) for e in b if a_dict.get(e)]
    return result
