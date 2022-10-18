def minimumBribes(q):
    bribes = 0

    for i, a in enumerate(q):
        i_adj = i + 1

        if a - i_adj > 2:
            print("Too chaotic")
            return
        
        for b in q[max(a-2, 0):i]:
            if b > a:
                bribes += 1
            
    print(bribes)
                
if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
