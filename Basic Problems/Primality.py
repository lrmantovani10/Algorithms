import math
import os

def primality(n):
    if n == 1:
        return "Not prime"
    elif 1 < n < 4:
        return "Prime"
    elif n % 2 == 0 or n % 3 == 0:
        return "Not prime"
    elif n > 10 and n % 7 ==0 and n % 5 == 0:
        return "Not prime"
    else:
        a = 5
        limit = math.sqrt(n)
        while a <= limit:
            if n % a == 0:
                return "Not prime"
            a += 2
        return "Prime"
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    p = int(input().strip())

    for p_itr in range(p):
        n = int(input().strip())

        result = primality(n)

        fptr.write(result + '\n')

    fptr.close()