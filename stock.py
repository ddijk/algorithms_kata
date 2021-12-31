def max_profit(arr):
    if not len(arr):
        return None

    max_prof = 0

    lowest =  arr[0]

    for i in arr[1:]: 
        if i < lowest:
            lowest = i
        else:
            if i-lowest > max_prof:
                max_prof = i -lowest
        
    return max_prof
