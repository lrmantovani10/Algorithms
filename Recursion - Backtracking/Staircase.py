import os

def stepPerms(n):
    memory = n * [0]
    def one_step(steps):
        if steps == 1:
            return 1
        elif steps == 2:
            return 2
        elif steps == 3:
            return 4
        else:
            if memory[steps - 1] == 0:
                total = one_step(steps - 3) + one_step(steps - 2) + one_step(steps - 1)
                memory[steps - 1] = total
            else:
                total =  memory[steps - 1]
            return total
    
    return one_step(n) % (10**10 + 7)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = int(input().strip())

    for s_itr in range(s):
        n = int(input().strip())

        res = stepPerms(n)

        fptr.write(str(res) + '\n')

    fptr.close()