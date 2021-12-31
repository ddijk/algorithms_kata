
def max_prod(arr):

    max = 0
    max_2nd = 0  # een na hoogste
    min = 0
    min_2nd = 0  # een na laagste

    for e in arr:
        if e > 0 and e > max:
            max_2nd = max
            max = e
            continue
        if e > 0 and e > max_2nd:
            max_2nd = e
        
        if e < 0 and e < min:
            min_2nd = min
            min = e
            continue
        if e < 0 and e < min_2nd:
            min_2nd = e

    max_pos = max * max_2nd
    max_neg = min * min_2nd

    print(f'max_pos is {max_pos}')
    print(f'max_neg is {max_neg}')

    return max_pos if max_pos > max_neg else max_neg
#[5, -10, 6, 9, 4])