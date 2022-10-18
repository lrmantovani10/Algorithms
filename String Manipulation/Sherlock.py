
import os

def isValid(s):
    s_dict = dict()
    for _, a in enumerate(s):
        if a not in s_dict:
            s_dict[a] = 1
        else:
            s_dict[a] += 1
            
    count_dict = dict()
    for a, b in s_dict.items():
        if str(b) not in count_dict:
            count_dict[str(b)] = 1
        else:
            count_dict[str(b)] += 1
    dict_keys = list(sorted(count_dict.keys(), key = lambda x: count_dict[str(x)]))
    if len(dict_keys) == 1:
        return "YES"
    elif len(dict_keys) == 2:
        first = count_dict[dict_keys[0]]
        second = count_dict[dict_keys[1]]
        if first != 1 and second != 1:
            return "NO"
        else:
            if first == second:
                return "YES"
            else:
                if first == 1 and int(dict_keys[0]) - 1 == int(dict_keys[1]) or int(dict_keys[0]) - 1 == 0:
                    return "YES"
                    
                elif second == 1 and int(dict_keys[1]) - 1 == 0:
                    return "YES"
                return "NO"
                    
    else:
        return "NO"
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()