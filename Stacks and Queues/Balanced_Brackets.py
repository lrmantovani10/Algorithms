import os

def isBalanced(s):
    forward = ["(","{","["]
    opposites = {")":"(","}":"{","]":"["}
    counts = {"(":0, ")":0, "[":0, "]":0, "{":0, "}":0}
    forwards = []
    for a in s:
        if a in forward:
            forwards.append(a)
        else:
            if len(forwards) > 0 and opposites[a] != forwards[-1]:
                return "NO"
            elif len(forwards) > 0:
                forwards.pop()
        counts[a] += 1
    for a,b in opposites.items():
        if counts[a] != counts[b]:
            return "NO"
    return "YES"
                
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
