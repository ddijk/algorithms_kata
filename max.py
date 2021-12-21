import sys

def max(a):
    if len(a) == 1:
         return a[0]
    m = max(a[1:])
    if a[0] > m :
        return a[0]
    else:
        return m

def main():
    print(max(map(int, sys.argv[1:])))

if __name__=='__main__':
    main()
