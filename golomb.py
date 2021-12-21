import sys

def golomb(n, memo={}):
    if n == 1:
        return 1

    if not memo.get(n):
         res = 1 + golomb(n - golomb(golomb(n - 1)))
         memo[n]=res

    return memo[n]

def main():
    print(golomb(int(sys.argv[1])))

if __name__=='__main__':
    main()

