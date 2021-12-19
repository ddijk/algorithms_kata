import sys

def print_numbers(a):
    result = []
    prt_numbers(a, result)
    return result

def prt_numbers(a,result):
    for e in a:
        if type(e) == int:
            result.append(e)
        else:
            prt_numbers(e, result)

