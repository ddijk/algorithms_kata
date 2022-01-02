
def sort(arr):
    for i in range(len(arr)):
        for j in range(i, 1, -1):
#            print(f'i={i} en j={j}')
            if arr[j] < arr[j-1]:
                temp = arr[j]
                arr[j]=arr[j-1]
                arr[j-1]= temp

    return arr


def main():
    input = [1,3,2,5,8,6,4,7]
    print(f'input = {input} ')
    print(sort(input))


if __name__ == '__main__':
    main()
