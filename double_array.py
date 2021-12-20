def double_array(a, index = 0):

    if len(a) == index:
        return a 
    else:
        a[index] *= 2
        return double_array(a, index+1)
