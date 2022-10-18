import os

def arrayManipulation(n, queries):
    arr = [0] * n
    for e in queries:
        arr[e[0] - 1] += e[2]
        if e[1] < len(arr):
            arr[e[1]] -= e[2]
    acc = 0
    big = 0
    for e in arr:
        if acc + e > big:
            big = acc + e 
        acc += e
    return big 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
