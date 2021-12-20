def double_array(a):

    return double_arr(a, 0)

def double_arr(a, index):
    if len(a) == index:
        return a 
    else:
        a[index] *= 2
        return double_arr(a, index+1)
