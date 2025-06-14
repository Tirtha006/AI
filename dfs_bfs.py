# Input graph directly 
graph = {} 
n = int(input("Enter number of nodes: ")) 
 
print("Enter node and its neighbors (space-separated). If no neighbors, just enter the node:") 
for _ in range(n): 
    parts = input().split() 
    node = parts[0] 
    neighbors = parts[1:] if len(parts) > 1 else [] 
    graph[node] = neighbors 
 
# Input start node 
start_node = input("Enter starting node: ") 
 
# BFS 
visited = [] 
queue = [] 
 
print("\nBreadth-First Search:") 
visited.append(start_node) 
queue.append(start_node) 
 
while queue: 
    m = queue.pop(0) 
    print(m, end=" ") 
    for neighbour in graph[m]: 
        if neighbour not in visited: 
            visited.append(neighbour) 
            queue.append(neighbour) 
 
# DFS 
visited = set() 
 
print("\n\nDepth-First Search:") 
 
def depthFirstSearch(graph, node): 
    if node not in visited: 
        print(node, end=" ") 
        visited.add(node) 
        for neighbour in graph[node]: 
            depthFirstSearch(graph, neighbour) 
 
depthFirstSearch(graph, start_node) 
