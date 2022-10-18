import os

def riddle(arr):
    
    # Total array length
    n = len(arr)
    
    # Finding the next greatest element
    next_greatest = [0] * n
    stack = []
    for i, el in enumerate(arr):
        if not stack or stack[-1][0] <= el:
            stack.append([el, i])
        else:
            while stack and stack[-1][0] > el:
                popped = stack.pop()
                next_greatest[popped[1]] = i  
            stack.append([el, i])
             
    while len(stack) > 0:
        popped = stack.pop()
        next_greatest[popped[1]] = len(arr)
    
    
    # Finding the previous smallest element
    prev_smallest = [0] * n
    stack = []
    for i, el in enumerate(arr[::-1]):
        a_i = n - 1 -i
        if not stack or stack[-1][0] <= el:
            stack.append([el, a_i])
        else:
            while stack and stack[-1][0] > el:
                popped = stack.pop()
                prev_smallest[popped[1]] = a_i
            stack.append([el, a_i])
                
    while len(stack) > 0:
        popped = stack.pop()
        prev_smallest[popped[1]] = -1
        
    # Finding the windows
    output_arr = [0] * (n +1)
    for i in range(n):
        # Width (we exclude the current element, so - 1)
        width = next_greatest[i] - prev_smallest[i] - 1
        output_arr[width] = max(arr[i], output_arr[width])
    
    # Dealing with larger / smaller windows
    for i in range(n - 1, 0, -1):
        output_arr[i] = max(output_arr[i], output_arr[i + 1])
    
    output_arr.pop(0)
    return output_arr
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = riddle(arr)

    fptr.write(' '.join(map(str, res)))
    fptr.write('\n')

    fptr.close()