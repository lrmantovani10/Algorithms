import os

def get_median(arr, d, med):
    pos = 0
    count = 0
    while count < med:
        count += arr[pos]
        pos += 1
    pos -= 1
    if d % 2 != 0 or count > med:
        return pos
    else:
        return (2*pos + 1)/2
def activityNotifications(expenditure, d):
    total = 0
    counts_list = [0] * 201
    for el in expenditure[:d]:
        counts_list[el] += 1
    if d % 2 == 0:
        middle = int(d / 2)
    else:
        middle = int(d / 2) + 1
    end = d
    current = 0
    while end < len(expenditure):
        median = get_median(counts_list, d, middle)
        if expenditure[end] >= (2 * median):
            total += 1
        counts_list[expenditure[end]] += 1
        counts_list[expenditure[current]] -= 1
        end += 1
        current += 1
    return total

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)

    fptr.write(str(result) + '\n')

    fptr.close()