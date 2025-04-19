# simulation/utils.py
from collections import defaultdict

# Make a graph

graph = {
    'W1':{'W2':2,'W3':3,'C1':1},
    'W2':{'W1':2,'W4':5,'C2':1},
    'W3':{'W1':3,'W4':3,'C3':1},
    'W4':{'W2':5,'W3':3,'W5':2,'C4':1},
    'W5':{'W4':2,'C5':1},
    'S1':{'W1':1,'W2':2,'W3':3,'W4':4,'W5':5},
    'S2':{'W1':2,'W2':1,'W3':3,'W4':4,'W5':5},
    'S3':{'W1':4,'W2':3,'W3':2,'W4':3,'W5':5},
    'S4':{'W1':4,'W2':3,'W3':2,'W4':1,'W5':3},
    'S5':{'W1':5,'W2':4,'W3':3,'W4':2,'W5':1},
    'C1':{},
    'C2':{},
    'C3':{},
    'C4':{},
    'C5':{},
}

'''
Warehouse pincodes
110001
290001
373301
494101
533101

Customer pincodes
110001
220002
330003
440004
550005

Supplier pincodes
110001
290002
373303
494104
533105
'''



# Generate best next warehouse from current to destination - pincode wise; return cost and next_warehouse

import heapq

def dijkstra(graph, start, end):
    # Priority queue to select the node with the smallest distance
    queue = [(0, start, [])]  # (cumulative_cost, current_node, path)
    visited = set()

    while queue:
        cost, node, path = heapq.heappop(queue)

        if node in visited:
            continue
        visited.add(node)

        path = path + [(node, cost)]  # append current node with cumulative cost

        if node == end:
            steps = [path[0]]
            for i in range(1, len(path)):
                prev_node, prev_cost = path[i-1]
                curr_node, curr_cost = path[i]
                step_cost = curr_cost - prev_cost
                steps.append((curr_node,step_cost))
            return cost, steps

        for neighbor, weight in graph[node].items():
            if neighbor not in visited:
                heapq.heappush(queue, (cost + weight, neighbor, path))

    return (float("inf"), [])  # If no path found

print(dijkstra(graph,'W1','C5'))

def get_next_position(current, destination):
    
    total_cost,steps = dijkstra(graph,current,destination)
    if len(steps)==1:
        return None,0
    return steps[1][0],steps[1][1]
