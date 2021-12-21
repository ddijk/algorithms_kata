import sys

def sum(array):
# Base case: only one element in the array: 
    if len(array) == 1:
        return array[0]
    return array[0] + sum(array[1:len(array)]) 

def main():

    input =sys.argv[1:]
    print('input is ',input)
    print(sum(map(lambda e: int(e), input)))

if __name__=='__main__':
    main()
