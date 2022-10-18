import os

def sockMerchant(n, ar):
    # Write your code here
    history = list()
    total = 0
    for s in ar:
        if s not in history:
            history.append(s)
            count = ar.count(s)
            if count % 2 == 0:
                addition_pairs = count / 2
                total += addition_pairs
            elif (count -1) % 2 == 0 and (count -1) / 2 != 0:
                total += (count -1)/2
                
    return int(total)
                
        
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()