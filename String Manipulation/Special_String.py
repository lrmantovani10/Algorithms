import os

# Complete the substrCount function below.
def substrCount(n, s):
    total = 0
    i = 0
    # First Case
    while i < n:
        count = 1
        while(i + 1 < n and s[i] ==  s[i + 1]):
            count += 1
            i += 1
        i += 1
        total += int((count * (count + 1))/2)
        
    # Second Case
    for index in range(1, n):
        i = 1
        while (index + i < n) and (index - i >= 0) and s[index] != s[index - 1] and s[index - i] == s[index + i] and s[index - 1] == s[index - i]:
            i += 1
        total += (i - 1)
    
    
    return total
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = substrCount(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
