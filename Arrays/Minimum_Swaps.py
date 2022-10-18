import os

def minimumSwaps(arr):
    swaps = 0
    ascending = []
    for a in arr:
        ascending.append(a)
    ascending.sort()
    while arr != ascending:
        for i,e in enumerate(arr):
            if e != i + 1:
                arr[e - 1], arr[i] = arr[i], arr[e-1]
                swaps += 1
    return swaps
                
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()