import os

def triplets(a, b, c):
    count = 0
    a = sorted(set(a))
    b = sorted(set(b))
    c = sorted(set(c))
    count = 0
    count_a = 0
    count_c = 0
    for e_b in b:
        while count_a < len(a) and a[count_a] <= e_b:
            count_a += 1
        while count_c < len(c) and c[count_c] <= e_b:
            count_c += 1
        
        count += (count_a * count_c)
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    lenaLenbLenc = input().split()

    lena = int(lenaLenbLenc[0])

    lenb = int(lenaLenbLenc[1])

    lenc = int(lenaLenbLenc[2])

    arra = list(map(int, input().rstrip().split()))

    arrb = list(map(int, input().rstrip().split()))

    arrc = list(map(int, input().rstrip().split()))

    ans = triplets(arra, arrb, arrc)

    fptr.write(str(ans) + '\n')

    fptr.close()
