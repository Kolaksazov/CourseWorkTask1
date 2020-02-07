if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    arr1 = list(arr)

    max = -1000
    secondMax = -100000

    for i in arr1:
        if (i > max):
            max = i

    for j in arr1:
        if (j > secondMax and j < max):
            secondMax = j

    print(secondMax)



