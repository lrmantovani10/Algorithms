import os

def maxMin(k, arr):
    arr.sort()
    comparator = (10**9)
    i = k
    while i <= len(arr):
        first = arr[i - k]
        second = arr[i - 1]
        if second - first < comparator:
            comparator =  second - first
        i += 1
    return comparator

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    k = int(input().strip())

    arr = []

    for _ in range(n):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = maxMin(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
