import os

def jumpingOnClouds(c):
    index = 0
    cloud = 0
    total_moves  = 0
    for element in c:
        if index == cloud and index < len(c) - 1:
            try:
                if c[index + 2] == 0:
                    cloud += 2
                    total_moves += 1
                elif c[index + 1] == 0:
                    cloud += 1
                    total_moves += 1
            except:
                try:
                    if c[index + 1] == 0:
                        cloud += 1
                        total_moves += 1
                except:
                    pass
                    
            
        index += 1
    
    return int(total_moves)
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()