import os

def getMinimumCost(k, c):
    c.sort(reverse = True)
    total = 0
    arr = [0] * k
    index = 0
    for e in c:
        total += ((arr[index] + 1) * e)
        arr[index] += 1
        index += 1
        if index >= k:
            index = 0
    return total
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    minimumCost = getMinimumCost(k, c)

    fptr.write(str(minimumCost) + '\n')

    fptr.close()
