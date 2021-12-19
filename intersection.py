def intersect(a,b):
    result = []
    a_dict = {e: True for e in a}
    for e in b:
        if a_dict.get(e):
            result.append(e)
    return result
