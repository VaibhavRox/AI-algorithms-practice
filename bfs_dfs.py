from collections import deque
graph={}
def bfs(start):
    visited=set()
    queue=deque([start])
    print("-----------BFS traversal-----------")
    while queue:
        vertex=queue.popleft()
        if vertex not in visited:
            print(vertex,end=" ")
            visited.add(vertex)
            queue.extend(neighbor for neighbor in graph[vertex] if neighbor not in visited)

def dfs(start):
    visited=set()
    stack=[start]
    print("\n-----------DFS traversal-----------")
    while stack:
        vertex=stack.pop()
        if vertex not in visited:
            print(vertex,end=" ")
            visited.add(vertex)
            stack.extend(reversed(graph[vertex]))

def create_graph():
    n=int(input("Enter the number of edges:"))
    print("Enter the cities in the form A B:")
    for i in range(n):
        u,v=input().split()
        if u not in graph:
            graph[u]=[]
        graph[u].append(v)
        #if undirected graph
        if v not in graph:
            graph[v]=[]
        graph[v].append(u)
    print("The graph is :\n")
    for key,value in graph.items():
        for i in value:
            print(key,'->',i)
create_graph()
start=input("Enter starting city:")
x=int(input("1. BFS traversal, 2. DFS traversal"))
if x==1:
    bfs(start)
elif x==2:
    dfs(start)
