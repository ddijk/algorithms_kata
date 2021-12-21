import sys

def golomb(n):
    if n == 1:
        return 1

    return 1 + golomb(n - golomb(golomb(n - 1)))

def main():
    print(golomb(int(sys.argv[1])))

if __name__=='__main__':
    main()

