import math
import os

def sherlockAndAnagrams(s):
    n = 0
    substring_dict = dict()
    for i1,a in enumerate(s):
        temp = ""
        for b in s[i1:]:
            temp += b 
            tempy = temp
            tempy = "".join(sorted(temp, key = str.lower))
            if tempy not in substring_dict:
                substring_dict[tempy] = 1
            else:
                substring_dict[tempy] += 1
    print(substring_dict)
    for a in substring_dict.values():
        if  a> 1:
            n += math.factorial(a)/(math.factorial(a - 2) * math.factorial(2))
    return int(n)
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()
