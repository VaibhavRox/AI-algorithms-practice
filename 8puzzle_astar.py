import heapq
def manhattan(state,goal):
    dist=0
    for i in range(9):
        if state[i]!=0:
            x1,y1=i//3,i%3
            x2,y2=goal.index(state[i])//3,goal.index(state[i])%3
            dist+=abs(x1-y1)+abs(y1-y2)
    return dist

#find next moves
def get_neighbours(state):
    neighbours=[]
    #find the zero
    idx=state.index(0)
    x,y=idx//3,idx%3
    moves=[(-1,0,'Up'),(1,0,'Down'),(0,-1,'Left'),(0,1,'Right')]
    for dx,dy,actions in moves:
        nx,ny=x+dx,y+dy
        if 0<=nx<3 and 0<=ny<3:
            new_idx=nx*3+ny
            new_state=list(state)
            new_state[idx],new_state[new_idx]=new_state[new_idx],new_state[idx]
            neighbours.append((tuple(new_state),actions))
    return neighbours

def astar(start,goal):
    pq=[]
    visited=set()
    heapq.heappush(pq,(manhattan(start,goal),0,start,[],[])) #f(n),g(n),state,path,moves
    while pq:
        f,g,state,path,move=heapq.heappop(pq)
        if state in visited:
            continue
        visited.add(state)
        if state==goal:
            return path+[state],move
        #append neightbours
        for neighbour,action in get_neighbours(state):
            if neighbour not in visited:
                new_g=g+1
                new_f=new_g+manhattan(neighbour,goal)
                heapq.heappush(pq,(new_f,new_g,neighbour,path+[state],move+[action]))
    return None,None

def read_input(state):
    puzzle=[]
    #we store the puzzle state as a flattened tuple of 9 indices
    print(f"Enter the {state} state:(3 rows, space separated, 0 for blank)")
    for _ in range(3):
        row=list(map(int,input().strip().split()))
        puzzle.extend(row)
    return tuple(puzzle)
print("-------------8puzzle using A*--------------\n")
start=read_input("start")
goal=read_input("goal")
solution,moves=astar(start,goal)
if solution:
    print(f"Solution exists!!\n Number of moves:{len(solution)-1} moves:\n")
    for i,state in enumerate(solution):
        for r in range(0,9,3):
            print(state[r:r+3])
        if i<len(moves):
            print(f"Move: {moves[i]}\n")
        print()
else:
    print("No solution exists!!")
