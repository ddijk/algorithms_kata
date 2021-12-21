def first(input):
    if not len(input): 
        return -1

    if input[0] == 'x':
        return 0

    return 1+first(input[1:])
