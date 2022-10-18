import os

def freqQuery(queries):
    data_structure = dict()
    counts = dict()
    output = []
    for q in queries:
        if q[0] == 1:
            if str(q[1]) not in data_structure:
                data_structure[str(q[1])] = 1
                if str(1) not in counts:
                    counts[str(1)] = 1
                else:
                    counts[str(1)] += 1
            else:
                data_structure[str(q[1])] += 1
                if str(data_structure[str(q[1])]) not in counts:
                    counts[str(data_structure[str(q[1])])] = 1
                else:
                    counts[str(data_structure[str(q[1])])] += 1
                if str(data_structure[str(q[1])] - 1) in counts:
                    counts[str(data_structure[str(q[1])] - 1)] -= 1
        elif q[0] == 2:
            if str(q[1]) in data_structure and data_structure[str(q[1])] > 0:
                data_structure[str(q[1])] -= 1
                if str(data_structure[str(q[1])] + 1) in counts:
                    if counts[str(data_structure[str(q[1])] + 1)] > 0:
                        counts[str(data_structure[str(q[1])] + 1)] -= 1
                if str(data_structure[str(q[1])]) in counts:
                    counts[str(data_structure[str(q[1])])] += 1
                else:
                    counts[str(data_structure[str(q[1])])] = 1
        elif q[0] == 3:
            if str(q[1]) in counts and counts[str(q[1])] > 0:
                output.append(1)
            else:
                output.append(0)
    return output
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = freqQuery(queries)

    fptr.write('\n'.join(map(str, ans)))
    fptr.write('\n')

    fptr.close()
