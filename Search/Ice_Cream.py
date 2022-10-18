def whatFlavors(cost, money):
    index_dict = dict()
    for i,c in enumerate(cost):
        if str(c) not in index_dict:
            index_dict[str(c)] = [i + 1]
        else:
            index_dict[str(c)].append(i + 1)
            
        if str(money - c) not in index_dict:
            index_dict[str(money - c)] = []
            
    if money %2 == 0 and str(int(money / 2)) in index_dict and len(index_dict[str(int(money / 2))])> 1:
        a_list = index_dict[str(int(money / 2))]
        a_list.sort()
        print(a_list[0], a_list[1])
        return
    
    for c in cost:
        if len(index_dict[str(money - c)]) > 0 and c != (money - c):
            response = [index_dict[str(c)], index_dict[str(money - c)]]
            response.sort()
            print(response[0][0], response[1][0])
            break 
            
    
if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        money = int(input().strip())

        n = int(input().strip())

        cost = list(map(int, input().rstrip().split()))

        whatFlavors(cost, money)
