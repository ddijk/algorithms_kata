def str_len(a):
    if not len(a):
        return 0

    return len(a[0]) + str_len(a[1:])
