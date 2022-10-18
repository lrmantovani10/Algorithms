import os

def repeatedString(s, n):
    if len(s) < n:
        remainder = n % len(s)
        whole_division = int(n / len(s))
        if remainder != 0:
            index = 0
            total_count = s.count('a') * whole_division
            for character in s:
                if index <= remainder - 1 and 'a' in character:
                    total_count += 1
                elif index > remainder -1:
                    break
                index += 1
            return total_count
        else:
            return s.count('a') * whole_division
                    
                
    elif len(s) == n:
        extended_s = s
    else:
        extended_s = s[0:n]
    
    total_a = extended_s.count('a')
    
    return int(total_a)
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input().strip())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
