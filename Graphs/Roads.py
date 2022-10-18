import os

def roadsAndLibraries(n, c_lib, c_road, cities):
    road_graph = dict()
    for road in cities:
        road1 = str(road[0])
        road2 = str(road[1])
        
        if road1 in road_graph:
            road_graph[road1].append(road2)
        else:
            road_graph[road1] = [road2]
            
        if road2 in road_graph:
            road_graph[road2].append(road1)
        else:
            road_graph[road2] = [road1]
    
    separate_groups = []
    history = set()
    def get_conn(n_str, set_acc):
        if n_str not in history:
            history.add(n_str)
            set_acc.add(n_str)
            for s in road_graph[n_str]:
                set_acc.update(get_conn(s, set_acc))
        return set_acc    
    
    for i in range(1, n + 1):
        i_str = str(i)
        if i_str not in road_graph:
            road_graph[i_str] = []
        if i_str not in history:
            separate_groups.append(get_conn(i_str, set()))
        
    print(separate_groups)   
    
    cost = 0
    for connection in separate_groups:
        conn_length = len(connection)
        all_lib = c_lib * conn_length
        i_roads = c_lib + ((conn_length - 1) * c_road)
        cost += min(all_lib, i_roads)
        
    return cost

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        c_lib = int(first_multiple_input[2])

        c_road = int(first_multiple_input[3])

        cities = []

        for _ in range(m):
            cities.append(list(map(int, input().rstrip().split())))

        result = roadsAndLibraries(n, c_lib, c_road, cities)

        fptr.write(str(result) + '\n')

    fptr.close()