
def bubble_sort(a):

    while True:
        if not bubble_once(a):
            break
    
    return a

def bubble_once(a):
    changed = False
    for i, e in enumerate(a[:-1]):
          if a[i] > a[i+1]:
              changed = True
              swap(a, i)
    return changed

def swap(a, i):
    temp = a[i]
    a[i] = a[i+1]
    a[i+1]= temp
