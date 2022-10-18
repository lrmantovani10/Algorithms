import os

def commonChild(s1, s2):
    s1_len = len(s1)
    s2_len = len(s2)
    string_matrix = [[0 for _ in range(s1_len + 1)] for _ in range(s2_len + 1)]
    for i1 in range(s1_len + 1):
        for i2 in range(s2_len + 1):
            if i1 == 0 or i2 == 0:
                string_matrix[i1][i2] = 0
            elif s1[i1 - 1] == s2[i2 - 1]:
                string_matrix[i1][i2] = 1 + string_matrix[i1 - 1][i2 - 1]
            else:
                string_matrix[i1][i2] = max(string_matrix[i1 - 1][i2], string_matrix[i1][i2 - 1])
    
    return string_matrix[-1][-1]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()

    s2 = input()

    result = commonChild(s1, s2)

    fptr.write(str(result) + '\n')

    fptr.close()
