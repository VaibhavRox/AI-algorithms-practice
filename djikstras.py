import heapq
distances={}
path={}
def initialize_distances(graph,start):
    for node in graph:
        distances[node]=float('inf')
        path[node]=[]  # Initialize path for each node
    distances[start]=0 #as distance of starting node to itself is ZERO

def djikstra(graph,start):
    initialize_distances(graph,start)
    pq=[]
    heapq.heappush(pq,(0,start))        #push in form of distance and node
    while pq:
        curr_dist,curr_node=heapq.heappop(pq)
        if curr_dist>distances[curr_node]: #if current travelled distance greater than stored distance, no need to go that way
            continue
        for neighbour,weight in graph[curr_node]:
            d=curr_dist+weight
            if d<distances[neighbour]:  #if travelled distance is less than stored, update that bih
                distances[neighbour]=d
                path[neighbour]=path[curr_node]+[curr_node]
                heapq.heappush(pq,(d,neighbour))

graph={}
num_node=int(input("Enter number of nodes:"))
for _ in range(num_node):
    node=input("Enter name of node:")
    graph[node]=[]
edges=int(input("Enter the number of edges:"))
print("Enter the data as starting ending weight, spaced:")
for _ in range(edges):
    u,v,w=input().split()
    # Ensure both nodes exist in graph (in case they weren't added during node input)
    if u not in graph:
        graph[u] = []
    if v not in graph:
        graph[v] = []
    graph[u].append((v,int(w)))
    graph[v].append((u,int(w)))
start=input("Enter the start node:")
djikstra(graph,start)
print("Shortest distance of each node from start node ",start)
for node in graph:
    if distances[node] != float('inf'):  # Only add node to path if it's reachable
        path[node].append(node)
    print(f"{start}->{node}:{distances[node]},Path:{path[node]}")