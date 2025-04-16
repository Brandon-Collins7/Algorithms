
from collections import deque
import time


adj = {} #adjacency list
lastNode = 0

with open('test_case_assignment2.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        node1, node2 = line.split(",")
        node1 = int(node1[2:])
        node2 = int(node2[2:])
        lastNode = max(lastNode, node2, node1)
        
        if node1 not in adj:
            adj[node1] = [node2]
        else:
            adj[node1].append(node2)
        if node2 not in adj:
            adj[node2] = [node1]
        else:
            adj[node2].append(node1)

def dfs(start, end):
    stack = [start]
    visited = set()
    visited.add(start)
    dist = 0
    
    while stack:
        node = stack.pop()
        dist += 1
        for nbr in adj[node]:
            if nbr == end:
                return dist + 1
            if nbr not in visited:
                visited.add(nbr)
                stack.append(nbr)
    
    return -1 #not reachable

def bfs(start, end):
    queue = deque([start])
    visited = set()
    visited.add(start)
    
    dist = 0
    
    while queue:
        
        node = queue.popleft()
        dist += 1
        for nbr in adj[node]:
            if nbr == end:
                return dist + 1
            if nbr not in visited:
                visited.add(nbr)
                queue.append(nbr)
    
    return -1 #not reachable
    
    

for i in range(1, lastNode + 1):
    
    #time.time_ns() seemed to be imprecise for small values
    start = time.perf_counter_ns()
    dist = dfs(0, i)
    end = time.perf_counter_ns()
    
    elapsed = (end - start) / 1e6

    #distance is the number of nodes visited before reaching the target node
    print(f"DFS: (0, {i}) - Distance: {dist}   Time: {elapsed} ms")
    
for i in range(1, lastNode + 1):
    
    #time.time_ns() seemed to be imprecise for small values
    start = time.perf_counter_ns()
    dist = bfs(0, i)
    end = time.perf_counter_ns()
    
    elapsed = (end - start) / 1e6

    print(f"BFS: (0, {i}) - Distance: {dist}  Time: {elapsed} ms")