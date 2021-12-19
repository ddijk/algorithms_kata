import string

def find_duplicate(a):
    map = {}
    for e in a:
        if map.get(e):
            return e
        else:
            map[e]=True
    return None


# input contains all letters of alphabet, except one
# return the missing letter
def find_missing_letter(sentence):
    for e in string.ascii_lowercase:
        if not e in sentence:
            return e

    return None

# find first non-duplicated char in string
def find_first_non_duplicated_char(input):
    map = {}
    for e in input:
        if map.get(e):
            map[e] += 1
        else:
            map[e]=1

    for e in input:
        if map[e] == 1:
            return e

    return None