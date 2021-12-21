# workaround for Python's way of handling default parameters:
# they are like instance members, they save state.
# Therefore when I called the original function twice without 'result' parameter,
# 'reult' is not empty, the second (and later) time.
def anagrams(input):
    return anagrams_(input, [])

def anagrams_(input, result=[]):
    if not len(input):
        return result

    if not len(result):
        result.append(input[0])
        return anagrams_(input[1:], result)
    
    result = add_one_to_result(input[0], result)
    return anagrams_(input[1:], result)

def add_one_to_result(letter, result):
    return [x for sublist in  map(lambda e: add_one_per_word(letter, e), result) for x in sublist]

# calculate all permutations of letter with the intermediate (shorter) anagrams
def add_one_per_word(letter, item):
    return map(lambda i: item[:i]+letter+item[i:], [e for e in range(len(item)+1)])
    
    
