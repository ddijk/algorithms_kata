
def reverse(input):
    if len(input)==1:
        return input
    else:
        return reverse(input[1:])+input[0]

    
