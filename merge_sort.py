
def merge_sort(a):

    n = len(a)

    if n < 2:
        return a

    sorted_left = merge_sort(a[:n//2])
    sorted_right = merge_sort(a[n//2:])

    return merge(sorted_left, sorted_right)

def merge(a, b):
    if not a:
        return b
    
    if not b:
        return a

    result=[]

    n_a =len(a)
    n_b = len(b)

    i_a=0
    i_b=0
    for i in range(n_a + n_b):
        if i_a == len(a):
            result.extend(b[i_b:])
            return result

        if i_b == len(b):
            result.extend(a[i_a:])
            return result

        if a[i_a] < b[i_b]:
            result.append(a[i_a])
            i_a += 1
        else:
            result.append(b[i_b])
            i_b += 1



