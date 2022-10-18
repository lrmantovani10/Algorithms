import os

def largestRectangle(h):
    stack = []
    comparator = 0
    i = 0
    h.append(0)
    while i < len(h):
        if not stack or h[stack[-1]] < h[i]:
            stack.append(i)
            i += 1
        else:
            last_index = stack.pop()
            comparator = max(comparator, ((i - stack[-1] -1) if stack else i ) * h[last_index])
    
    return comparator
            
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    h = list(map(int, input().rstrip().split()))

    result = largestRectangle(h)

    fptr.write(str(result) + '\n')

    fptr.close()