def fibonacci(n):
    sequence = []
    for i in range(n + 1):
        if i < 2:
            sequence.append(i)
        else:
            sequence.append(sequence[i - 2] + sequence[i - 1])
    return sequence[n]

n = int(input())
print(fibonacci(n))
