import heapq
def a_star(graph,start,goal,heuristic):
    open_set=[]
    heapq.heappush(open_set,(0,start))

    g_score={node:float('inf')for node in graph}
    g_score[start]=0

    came_from={}

    while open_set:
        _,current=heapq.heappop(open_set)
        if current==goal:
            path=[]
            while current in came_from:
                path.append(current)
                current=came_from[current]
            path.append(start)
            return path[::-1]
        
        for neighbour,cost in graph[current].items():
            tentative_g_score=g_score[current]+cost
            if tentative_g_score<g_score[neighbour]:
                g_score[neighbour]=tentative_g_score
                came_from[neighbour]=current
                f_score=tentative_g_score+heuristic[neighbour]
                heapq.heappush(open_set,(f_score,neighbour))

    return None
graph={
    'A':{'B':1,'C':3},
    'B':{'D':1,'E':4},
    'C':{'F':2},
    'D':{'G':2},
    'E':{'G':1},
    'F':{'G':5},
    'G':{},

}
heuristic={
    'A':5,
    'B':4,
    'C':2,
    'D':1,
    'E':4,
    'F':2,
    'G':0
}
start_node='A'
goal_node='G'
path=a_star(graph,start_node,goal_node,heuristic)

if path:
    print(f"Shortest distance from {start_node}to{goal_node}:{path}")
else:
    print("No path found")

